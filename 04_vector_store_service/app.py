from langchain_chroma import Chroma
from config_data as config
from langchain_community.embeddings import DashScopeEmbeddings

# 类定义
class VectorStoreService(object):
  def __init__(self,embedding):
    self.embedding = embedding,
    self.vector_store = Chroma(
      collection_name = config.collection_name,
      embedding_function = self.embedding,
      persist_directory = config.persist_directory
    )

def get_retriever(self):
  return self.vector_store.as_retriever(search_kwargs={k:config_similarity_threshold})

#主程序测试
if __name__ == '__main__':
  retriever = VectorStoreService(DashScopeEmbeddings(model="text-embeddding-v4")).get_retriever()
  res = retriever.invoke("我180斤，尺码推荐")
  print(res)
  
