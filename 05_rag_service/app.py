from vector_store import VectorStoreService
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.chat_models import ChatTongyi
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
import config_data as config


def print_prompt(prompt)
  print("="*20)
  print(prompt.to_string())    #把拼好的prompt打印出来
  print("="*20)

  return prompt               #原样传给下一步
  
class RagService(object):
  def __init__(self):

    self.vector_service = VectorStoreService(
      embedding = DashScopeEmbeddings(model = config.embedding_model_name)

    self.prompt_template = ChatPromptTemplate(
      [
        ("system","以我提供的已知参考资料为主，"
         "简洁和专业的回答用户问题。参考资料：{context}"),
        ("user","请回答用户提问：{input}")

    self.chat_model = ChatTongyi(model = config.chat_model_name)

    self.chain = self.__get__chain(self)

    def __get__chain(self):
      retriever = self.vector_service.get_retriever()


    def format_document(docs:list[Document]):
      if not docs:
        return "无相关参考资料"

    formatted_str = ""
    for doc in docs:
      formatted_str += f"文档片段:{doc.page_content}"
      formatted_str += "\n"
      formatted_str += f"元数据:{doc.metadata}"
      formatted_str += "\n\n"

      return formatterd_str

   chain = (
     {
       "input":RunnablePassthrough(),
       "context":retriever | format_document
     } | self.prompt_template | print_prompt | self.chat_model | StrOutpurParser()
   )
  res = chain.invoke(input:{"我体重180斤，尺码推荐"})
  print(res)
    
  
