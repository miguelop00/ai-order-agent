# Agente para gestión de pedidos

### Versión 1.0

Esta primera versión del proyecto tiene como objetivo la creación de un agente conversacional, ya sea usando OpenAI o cualquier LLM open source, para que gestione datos de pedidos de clientes, y realice alguna función sencilla con ellos.En este caso, las funciones son:

1. Registrar pedidos:

El cliente pide una serie de elementos, y el agente los separa entre nombre, elementos y cantidad de cada uno, con el siguiente formato: {Nombre del cliente: {elemento1: cantidad1, elemento2: cantidad2,...}}. Esto se incluye en el docstring de la primera herramienta del   agente "crear_dict", y funciona como prompt.

La segunda herramienta consiste en tomar el diccionario generado por crear_dict, e incluirlo en el archivo JSON (pedidos.json), con el mismo formato. Esta herramienta se llama "registrar_pedido".

2. Dar información sobre un pedido:

Para esta función, hemos creado una herramienta llamada "info_pedidos", la cual recoge la información del archivo JSON generada antes, y selecciona el pedido en función del nombre del cliente.  



****




<div align="center">
  <img src="https://github.com/user-attachments/assets/8b1d3b0a-620d-48da-8aec-1b5e04558a2f" alt="chatbot1" width="300"/>   
  <img src="https://github.com/user-attachments/assets/63b8ff2a-1033-4e6c-b28b-6be805c97502" alt="chatbot1" width="300"/>
</div>

