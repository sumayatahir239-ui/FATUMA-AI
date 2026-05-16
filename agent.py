from dotenv import load_dotenv
import os
load_dotenv()
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage,AIMessage
api_key = os.getenv("GROQ_API_KEY")
llm =ChatGroq(api_key=api_key, model="llama-3.3-70b-versatile")
system_prompt="""
You are FATUMA built by Fatuma Tahir.You are intelligent AI assistant.You are helpful,consice,and conversational."""
messages=[
    SystemMessage(content=system_prompt)
]
print("Welcome to FATUMA(type'exit'to quit)")
while True:
    user_input=input("You:")
    if user_input.lower()=="exit":
        print("Goodbye")
        break
    messages.append(HumanMessage(content=user_input))
    response = llm.invoke(messages)
    print(f"FATUMA:{response.content}")
    messages.append(AIMessage(content=response.content))
                                        