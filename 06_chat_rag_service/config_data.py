"""
配置文件 - RAG 服务相关参数
"""
import os

# 当前文件所在目录的上级目录（项目根目录）
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Chroma 向量库持久化目录
persist_directory = os.path.join(BASE_DIR, "data", "chroma_db")

# 集合名称（类似数据库表名）
collection_name = "clothing_knowledge"

# 相似度检索返回的文档数量（top-k）
similarity_threshold = 3

# 嵌入模型名称（用于文本向量化）
embedding_model_name = "text-embedding-v4"

# 对话模型名称（用于生成回答）
chat_model_name = "qwen-max"
