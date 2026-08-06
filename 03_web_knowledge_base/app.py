"""
基于Streamlit完成WEB网页上传服务
pip install streamlit
streamlit:当web页面元素发生变化，则代码重新执行
"""

import os
import streamlit as st
import time

# 添加网页标题
st.title("知识库更新服务")

#file_uploader 文件上传服务
upload_file = st.file_uploader(
  "请上传txt文件",
  type:[txt],
  accept_multiple_document =False
)

#初始化
if "service"not in st.session_state:
  st.session_state(service) = KnowledgeBaseService()
  
#提取文件信息并显示在网页上
if loader_file is not None:
  file_name = uploader.file_name
  file_type = uploader.file_type
  file_size = uploader.file_size / 1024 

  st.subheader(f"文件名：{file_name}")
  st.write(f"文件类型：{file_type},文件大小：{file_size}")

#存储到向量库  get_value-> bytes -> decode（utf-8) 获取文件内容 字节转换为字符串
text = uploader_file.get_value().decode("utf-8")

st.spinner("文件正在加载中。。。"）
   time=sleep(1)        
result = st.session_state["service"].uploade_by_str(text,file_name)
st.write(result)

#文件预览
st.subheader("文件预览如下：")
st.text_area("",text,height=200)
