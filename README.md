# Order Management AI Agent

### Version 1.0

The aim of this first version of the project is to create a conversational agent, using either OpenAI or any open-source LLM, to manage customer order data and perform simple tasks with it. It is intended to improve the communication between client and business, making it 24/7 available for ordering. 

This project was designed for a Spanish company's use case, so all the examples are written in Spanish. Nevertheless, a simple translation of the prompts should be enough to make it work in any language available for the LLM.

Right now, the agent is capable of:

- Registering orders:

  The customer requests a series of items, and the agent separates them by name, items, and quantity of each, using the following format: {Customer Name: {item1: quantity1, item2: quantity2,...}}. This format is included in the docstring of the agent’s first tool,       "crear_dict", which also serves as a prompt.
  
  The dictionary is then added to a JSON file (pedidos.json) in the same format, by means of the second tool "registrar_pedido".

- Provide information about an existing order:

  For this function, we have created a tool called "info_pedidos", which retrieves information from the JSON file generated earlier and selects the order based on the customer’s name.
<br>

### Examples

To illustrate how it looks like, we have linked it to a Telegram bot, so we are able to send queries directly from our smartphone.
<br><br><br>
<div align="center">
  <img src="https://github.com/user-attachments/assets/8b1d3b0a-620d-48da-8aec-1b5e04558a2f" alt="chatbot1" width="300"/>   
  <img src="https://github.com/user-attachments/assets/63b8ff2a-1033-4e6c-b28b-6be805c97502" alt="chatbot1" width="300"/>
</div>
<br><br><br>

### Further work

  - Include memory context

  - Get metadata from Telegram to work by client id

  - Include more tools

  - Connect system for statistical recommendations

