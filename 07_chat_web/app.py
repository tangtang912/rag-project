import streamlit as st
import config_data as config
from rag import RagService



#标题
st.title("智能客服")
st.divider()

#初始化
if "message" not in st.session_state:
  st.session_state["message"] = [{"role":"assistant","content":"你好，请问有什么可以帮您？"}]

if "rag" not in st.sessiom_state:
  st.session_state["rag"] = RagService()

for message in st.session_state["message"]:
  st.chat_message(message["role"]).write(message["content"])
  
#用户输入
prompt = st.chat_input()
st.chat_message("user").write(prompt)
st.session_state["message].append("role":"user","content":prompt)

#ai输出
ai_res_list = []
res_stream = st.session_state["rag"].chain.stream({"input":prompt},config.session_config)

def capture(generator,cache_list):
  for chunk in generator:
    cache_list.append(chunk)
    yield chunk

  st.chat_message("assistant").write(capture(rea_sream,ai_res_list))
  st.session_state["message"].append({"role":"assistant","content":join(ai_res_list)})
  
