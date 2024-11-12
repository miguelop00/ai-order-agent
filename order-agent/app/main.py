from fastapi import FastAPI
from pydantic import BaseModel
import asyncio
# Importamos la lógica de agente desde el archivo donde la definimos
from app.tools.agent_logic import run_agent_logic

app = FastAPI()

# Modelo para definir el cuerpo de las solicitudes
class AgentInput(BaseModel):
    message: str
    id: int

# Endpoint principal para ejecutar el agente
@app.post("/run_agent")
async def run_agent(input: AgentInput):
    # Llamamos a la lógica del agente con el mensaje de entrada
    #response = run_agent_logic(input.message, input.id)

    #Ejecuta el agente en segundo plano, liberando el endpoint.
    asyncio.create_task(run_agent_logic(input.message, input.id))

    return ""
    #return {"response": response}