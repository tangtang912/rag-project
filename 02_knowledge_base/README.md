# 练习 02：知识库服务模块

## 功能说明
- 基于 Chroma 向量数据库实现本地知识存储
- 支持文本分割（长文本自动切段）
- MD5 去重（相同内容不重复存储）
- 自动记录上传时间、操作人、来源等元数据

## 文件结构
02_knowledge_base/
├── app.py # 主程序（KnowledgeBaseService 类）
├── config_data.py # 配置文件
└── README.md # 本说明文档

## 核心知识点
- `Chroma` 向量数据库的使用
- `RecursiveCharacterTextSplitter` 文本分割
- MD5 哈希去重
- 元数据管理（metadata）

## 运行
```bash
python app.py
