#现在我们已经构建了一个应用程序，我们需要提供服务。这就是 LangServe 的用武之地。 LangServe 帮助开发者将 LangChain 链部署为 REST API。您不需要使用 LangServe 来使用 LangChain，但在本指南中，我们将展示如何使用 LangServe 部署您的应用。

# 虽然本指南的第一部分旨在在 Jupyter Notebook 或脚本中运行，但我们现在将脱离这一点。我们将创建一个 Python 文件，然后从命令行与之交互。


#为了为我们的应用创建一个服务器，我们将制作一个 serve.py 文件。
# 
# 这个文件将包含我们服务应用的逻辑。它由三部分组成：
#为了为我们的应用创建一个服务器，我们将制作一个 serve.py 文件。这个文件将包含我们服务应用的逻辑。它由三部分组成：

#1.我们刚刚构建的链的定义
# 2我们的 FastAPI 应用
# 3.一个定义用于服务链的路由，这通过 langserve.add_routes 完成

from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langserve import add_routes

import getpass
import os
import langchain

from langchain.schema.messages import HumanMessage, SystemMessage,AIMessage

from langchain_openai import AzureChatOpenAI


# 1. Create prompt template
system_template = "Translate the following into {language}:"
prompt_template = ChatPromptTemplate.from_messages([
    ('system', system_template),
    ('user', '{text}')
])

# 2. Create model
model = AzureChatOpenAI(
    azure_endpoint="https://12205-m2hl4tqk-eastus.openai.azure.com/openai/deployments/gpt-35-turbo/chat/completions?api-version=2024-08-01-preview",
    azure_deployment="gpt-35-turbo",
    openai_api_version="2024-08-01-preview",
    api_key="d7f27353b3b3463bb02b2708df922f35",  
)

# 3. Create parser
parser = StrOutputParser()

# 4. Create chain
chain = prompt_template | model | parser


# 4. App definition
app = FastAPI(
  title="LangChain Server",
  version="1.0",
  description="A simple API server using LangChain's Runnable interfaces",
)

# 5. Adding chain route
add_routes(
    app,
    chain,
    path="/chain",
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)

    #每个 LangServe 服务都配有一个简单的 内置用户界面，用于配置和调用应用，支持流式输出并
    # 可查看中间步骤。 前往 http://localhost:8000/chain/playground/ 试用一下！输入与之前相同的内容
    #  - {"language": "italian", "text": "hi"} - 它应该会像之前一样响应。
    

    

    