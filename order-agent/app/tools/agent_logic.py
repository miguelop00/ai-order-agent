import nest_asyncio
import json
import os
import requests
from dotenv import load_dotenv
from app.config import config
from app.config import OPENAI_API_KEY, PEDIDOS_PATH
from llama_index.llms.openai import OpenAI
from llama_index.core.tools import FunctionTool
from llama_index.core.agent import FunctionCallingAgentWorker
from llama_index.core.agent import AgentRunner


def crear_dict(**kwargs):
    """Esta función toma todos los elementos requeridos y los añade a un diccionario con la siguiente forma: {id del cliente: {elemento1: cantidad1, elemento2: cantidad2,...}}.
     Ten en cuenta que las cantidades pueden venir en distintos formatos (1 elemento, 1 caja de elementos, 1 camión de elementos...)."""
    return dict(kwargs)


def registrar_pedido(id, diccionario):
    """Añade el diccionario a un archivo JSON existente y hace saber al cliente que su pedido está registrado, incluyendo los elementos del pedido en la respuesta.
    El diccionario creado antes es del formato {id del cliente: {elemento1: cantidad1, elemento2: cantidad2,...}}, así que las variables de la función son:
    id: id del cliente
    diccionario: {elemento1: cantidad1, elemento2: cantidad2,...}"""
    
    try:
        # Intenta leer el contenido actual del archivo JSON
         with open(PEDIDOS_PATH, 'r', encoding='utf-8') as archivo:
            contenido = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
         contenido = {}

    
    if id in contenido:
        for item, cantidad in diccionario.items():
            if item in contenido[id]:
                contenido[id][item] += cantidad
            else:
                contenido[id][item] = cantidad

    else:
        contenido[id] = diccionario    
    

    # Añade el nuevo diccionario al contenido existente
    #contenido.update(diccionario)

    #Escribe el contenido actualizado en el archivo JSON
    with open(PEDIDOS_PATH, 'w', encoding='utf-8') as archivo:
        json.dump(contenido, archivo, ensure_ascii=False, indent=4)


def info_pedidos():
    """Da información al cliente sobre los elementos de su pedido, a partir del contenido de un archivo JSON.""" 
    with open(PEDIDOS_PATH, 'r', encoding='utf-8') as archivo:
            contenido = json.load(archivo)
    return contenido


async def send_to_telegram(message:str, user_id:str):
    load_dotenv()

    TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

    bot_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {
        'chat_id': user_id,
        'text': message
    }

    response = requests.post(bot_url, data=data)
    if response.status_code != 200:
        print(f"Error al enviar mensaje a Telegram: {response.status_code}, {response.text}")


async def run_agent_logic(message, user_id):
    # Implementa aquí la lógica de tu agente. Por ejemplo:
    nest_asyncio.apply()
    agent_prompt = config.AGENT_PROMPT

    info_pedidos_tool = FunctionTool.from_defaults(fn=info_pedidos)
    registro_tool = FunctionTool.from_defaults(fn=registrar_pedido)
    crear_dict_tool = FunctionTool.from_defaults(fn=crear_dict)

    llm = OpenAI(api_key=OPENAI_API_KEY, model="gpt-3.5-turbo", temperature=0.3)
    agent_worker = FunctionCallingAgentWorker.from_tools(
        tools=[registro_tool, crear_dict_tool, info_pedidos_tool], 
        system_prompt=agent_prompt,
        llm=llm, 
        verbose=True
    )
    agent = AgentRunner(agent_worker)
    message_and_id = str(user_id) + ": " + message
    response = agent.chat(message_and_id)

    await send_to_telegram(response, user_id)