# from ollama import chat
# from ollama import ChatResponse

# stream: ChatResponse = chat(
#     model="glm-4.6:cloud",
#     messages=[
#         {
#             "role": "user",
#             "content": "Why is the sky blue?",
#         }
#     ],
#     stream=True,
# )
# for chunk in stream:
#     print(chunk["message"]["content"], end="", flush=True)



# Scrapper Function
# try:
#     from ..agent.src.agent.tools import browse_tool
# except ImportError:
#     import sys
#     import os
#     sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#     from agent.src.agent.tools import browse_tool

# response = browse_tool.run(url="https://example.com/")
# print(response)
