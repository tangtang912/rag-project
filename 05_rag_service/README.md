# 练习 05：RAG 检索增强生成服务 (RagService)

## 功能说明
- 结合向量检索与 LLM 生成，实现完整的 RAG 问答链路
- 用户提问 → 向量检索（从知识库获取相关文档）→ 组装提示词（上下文增强）→ LLM 生成专业回答
- 支持通过配置灵活调整嵌入模型和对话模型

## 文件结构
05_rag_service/
├── app.py # RagService 主程序
├── vector_store.py # 向量存储服务（从练习4复制）
├── config_data.py # 配置文件
└── README.md # 本说明文档

## 核心知识点
- **RAG 完整链路**：检索 → 增强 → 生成
- **LCEL 链式组合**：`{input, context} | prompt | model | parser`
- **`RunnablePassthrough`**：透传用户输入
- **`format_document`**：将检索结果格式化为可读文本

## 数据流图
用户提问 "我体重180斤，尺码推荐"
↓
┌─────┴─────┐
↓ ↓
"input" "context"
↓ ↓
透传 retriever → format_document
↓ ↓
└─────┬─────┘
↓
{input, context}
↓
ChatPromptTemplate
↓
print_prompt（调试打印）
↓
ChatTongyi 模型
↓
StrOutputParser
↓
最终回答

## 运行
```bash
python app.py
