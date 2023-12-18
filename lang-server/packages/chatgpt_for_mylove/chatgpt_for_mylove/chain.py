# 检索增强生成（RAG）: 扫描代码库
# 源码参考：https://python.langchain.com/docs/use_cases/question_answering/code_understanding
import logging


logging.basicConfig(level=logging.ERROR,filename="./gpt.log")
from langchain.chat_models import ChatOpenAI
llm = ChatOpenAI(
    model_name="gpt-4",
)

from langchain.pydantic_v1 import BaseModel

from langchain.schema.runnable import RunnableParallel, RunnablePassthrough

def logInfo(info):
    logging.error(info)
    return info

chain = (
        RunnablePassthrough()
        | logInfo
        | llm
        | logInfo
)

class InputType(BaseModel):
    __root__: str


chain = chain.with_types(input_type=InputType)
