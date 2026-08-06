# 练习 03：Web 上传 + 知识库服务整合

## 功能说明
将练习 1 的 Streamlit 文件上传界面与练习 2 的知识库服务整合：
- 用户通过 Web 界面上传 TXT 文件
- 系统自动提取文件内容，调用知识库服务进行向量化存储
- 支持 MD5 去重，避免重复入库
- 实时显示处理结果和文件内容预览

## 文件结构
03_web_knowledge_base/
├── app.py # Streamlit 主程序
├── knowledge_base.py # 知识库服务类（从练习2复制）
├── config_data.py # 配置文件（从练习2复制）
└── README.md # 本说明文档

## 核心知识点
- `st.session_state`：在 Streamlit 中保持跨重绘的状态
- `st.spinner`：提供加载动画，提升用户体验
- Streamlit + LangChain 的集成模式

## 运行
```bash
streamlit run app.py
