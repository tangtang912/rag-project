# 👕 服装商品智能客服系统

> 基于 **LangChain** + **Streamlit** + **DashScope** 构建的本地知识库问答系统，以“某东商品衣服”为例，让用户自由更新知识，答案基于本地知识生成。

---

## 🎯 项目目标

- 构建一个**可自由更新知识**的服装商品智能客服。
- 用户上传商品属性文档（如尺码表、面料说明、洗涤建议等），系统自动向量化存储。
- 用户提问时，系统从本地知识库中检索最相关的片段，并由大模型生成专业、准确的回答。

---

## 🧩 技术栈

| 组件 | 技术 |
| :--- | :--- |
| Web 界面 | Streamlit |
| LLM 模型 | 通义千问 (DashScope) |
| 嵌入模型 | text-embedding-v4 (DashScope) |
| 向量数据库 | Chroma（持久化） |
| 文档加载 | CSVLoader, PyPDFLoader, TextLoader |
| 文本分割 | RecursiveCharacterTextSplitter |
| 框架 | LangChain (LCEL) |

---

## 📂 项目列表

| 编号 | 文件夹 | 说明 | 核心知识点 |
| :---: | :--- | :--- | :--- |
| 01 | [01_file_upload](./01_file_upload) | Streamlit 文件上传服务 | `st.file_uploader`, 文件读取与解码 |
| 02 | [02_knowledge_base](./02_knowledge_base) | 知识库服务模块 | Chroma向量存储, 文本分割, MD5去重 |
| 03 | [03_web_knowledge_base](./03_web_knowledge_base) | Web上传+知识库整合 | Streamlit集成, session_state, 端到端流程 |
| 04 | [04_vector_store_service](./04_vector_store_service) | 向量存储服务封装 | Chroma独立封装, as_retriever, 配置驱动 |
| 05 | [05_rag_service](./05_rag_service) | RAG检索增强生成 | 完整RAG链路, LCEL组合, RunnablePassthrough |
| 06 | [06_chat_rag_service](./06_chat_rag_service) | 带对话记忆的RAG服务 | RunnableWithMessageHistory, MessagesPlaceholder, 会话管理 |

## 📂 项目结构
├── 01_file_upload/                    # ✅ 已创建
│   ├── app.py
│   └── README.md
│
├── 02_knowledge_base/                 # ✅ 已创建
│   ├── app.py
│   ├── config_data.py
│   └── README.md
│
├── 03_web_knowledge_base/             # ✅ 已创建
│   ├── app.py
│   ├── knowledge_base.py
│   ├── config_data.py
│   └── README.md
│
├── 04_vector_store_service/           # ✅ 已创建
│   ├── app.py
│   ├── config_data.py
│   └── README.md
│
├── 05_rag_service/                  # ✅ 已创建
│   ├── app.py                       # RagService 主程序
│   ├── vector_store.py              # 向量存储服务
│   ├── config_data.py               # 配置文件
│   └── README.md
│
├── 06_chat_rag_service/             # ✅ 已创建
│   ├── app.py                       # 主程序
│   ├── vector_store.py              # 向量存储服务
│   ├── config_data.py               # 配置文件
│   ├── file_history_store.py        # 对话历史存储
│   └── README.md

