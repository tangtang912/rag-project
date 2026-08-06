
md5_path = "./ md5.text"

#Croma
collection_name = "rag"
persist_directory = "./chroma_db"

#spliter
chunk_size = 1000
chunk_overlap = 100
separators = ["\n\n","\n",",",".","?","!","，","。","？","！"," ",""]
max_spliter_char_number = 1000       #文本分割的阈值

#相似度检索阈值
similarity_threshold = 2   # 返回检索值的文档数量
