# 练习 07：智能客服 Web 界面

## 功能说明
- 基于 Streamlit 构建智能客服聊天界面
- 集成练习6的带对话记忆的 RAG 服务
- 支持流式输出（逐字显示回答）
- 自动保存聊天历史，保持对话连贯性

## 文件结构
07_chat_web/
├── app.py # Streamlit 主程序
├── rag.py # RAG 服务类（从练习6复制）
├── vector_store.py # 向量存储服务（从练习4/5/6复制）
├── file_history_store.py # 对话历史存储（从练习6复制）
├── config_data.py # 配置文件
└── README.md # 本说明文档

## 核心知识点
- **Streamlit 聊天组件**：`st.chat_message()`、`st.chat_input()`
- **`write_stream()`**：Streamlit 原生流式输出支持
- **`st.session_state`**：在页面重绘间保持聊天历史和 RAG 服务实例
- **流式生成**：使用 `chain.stream()` 逐步输出回答

## 运行
```bash
cd 07_chat_web
streamlit run app.py
