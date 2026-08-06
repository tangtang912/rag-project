# 练习 04：向量存储服务封装 (VectorStoreService)

## 功能说明
- 独立封装 Chroma 向量数据库的初始化与检索器获取
- 将向量存储逻辑与业务逻辑分离，提高代码可维护性
- 通过 `get_retriever()` 方法返回标准 Retriever 对象，便于集成到 LCEL 链中

## 文件结构
04_vector_store_service/
├── app.py # VectorStoreService 类
├── config_data.py # 配置文件（含 similarity_threshold）
└── README.md # 本说明文档

## 核心知识点
- **单一职责原则**：将向量存储独立为服务类
- **`as_retriever()`**：将 Chroma 转换为 LCEL 兼容的 Retriever
- **`search_kwargs={"k":n}`**：控制检索返回的文档数量

## 运行
```bash
python app.py
