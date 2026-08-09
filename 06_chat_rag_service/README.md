# 练习 06：带对话记忆的 RAG 服务 (ChatRagService)

## 功能说明
- 在练习5的 RAG 服务基础上，增加**多轮对话记忆**功能
- 支持同一用户连续提问时保持上下文关联
- 通过 `RunnableWithMessageHistory` 和 `MessagesPlaceholder` 实现

## 文件结构
06_chat_rag_service/
├── app.py # 主程序（RagService 类）
├── vector_store.py # 向量存储服务（从练习4/5复制）
├── config_data.py # 配置文件
├── file_history_store.py # 对话历史存储模块（新增）
└── README.md # 本说明文档

## 核心知识点
- **`RunnableWithMessageHistory`**：LangChain 官方提供的对话记忆包装器
- **`MessagesPlaceholder("history")`**：在提示词中预留对话历史位置
- **`file_history_store.py`**：自定义历史存储模块（基于内存字典）
- **`session_id`**：区分不同用户的会话标识

## 数据流图
用户提问 + session_id
↓
{input, session_id}
↓
RunnableWithMessageHistory
（自动注入 history）
↓
构建链：与练习5相同
但 history 自动填充到 MessagesPlaceholder
↓
模型回答
↓
自动保存到历史
↓
返回用户

## 运行
```bash
python app.py
