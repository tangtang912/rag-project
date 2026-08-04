"""
配置文件 - 知识库服务相关参数
"""
import os

# 当前文件所在目录的上级目录（项目根目录）
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Chroma 向量库持久化目录
persist_directory = os.path.join(BASE_DIR, "data", "chroma_db")

# 集合名称（类似数据库表名）
collection_name = "clothing_knowledge"

# MD5 记录文件路径（用于去重）
md5_path = os.path.join(BASE_DIR, "data", "md5_records.txt")

# 文本分割参数
chunk_size = 500
chunk_overlap = 50
separators = ["\n\n", "\n", "。", "，", "！", "？", ".", "!", "?", " ", ""]

# 超过此字符数才进行分割（小于则直接作为一段）
max_spliter_char_number = 100
