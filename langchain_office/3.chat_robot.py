from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import getpass
import os
import langchain
from langchain.schema.messages import HumanMessage, SystemMessage,AIMessage
from langchain_openai import AzureChatOpenAI


# 2. Create model
model = AzureChatOpenAI(
    azure_endpoint="https://12205-m2hl4tqk-eastus.openai.azure.com/openai/deployments/gpt-35-turbo/chat/completions?api-version=2024-08-01-preview",
    azure_deployment="gpt-35-turbo",
    openai_api_version="2024-08-01-preview",
    api_key="d7f27353b3b3463bb02b2708df922f35",  
)



