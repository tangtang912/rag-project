"""
对话历史存储模块
用于管理不同会话（session）的聊天历史记录
"""
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import GetSessionHistoryCallable
from langchain_core.chat_history import BaseChatMessageHistory

# 全局字典，存储所有会话的历史记录
# key: session_id, value: ChatMessageHistory 对象
session_histories = {}


def get_history(session_id: str) -> BaseChatMessageHistory:
    """
    获取或创建指定会话的历史记录对象
    
    :param session_id: 会话唯一标识符（如 "user_001"）
    :return: ChatMessageHistory 对象
    """
    if session_id not in session_histories:
        # 如果该会话不存在，则创建新的历史记录
        session_histories[session_id] = ChatMessageHistory()
    
    return session_histories[session_id]


def clear_history(session_id: str) -> None:
    """
    清空指定会话的历史记录（可选功能）
    
    :param session_id: 会话唯一标识符
    """
    if session_id in session_histories:
        session_histories[session_id].clear()


def get_all_sessions() -> list:
    """
    获取所有活跃的会话ID列表（调试用）
    
    :return: 会话ID列表
    """
    return list(session_histories.keys())
