import getpass
import os

access_token = getpass.getpass(prompt="Access token: " + os.environ['AISTUDIO_ACCESS_TOKEN'])

from erniebot_agent.extensions.langchain.llms import ErnieBot

llm = ErnieBot(aistudio_access_token=access_token)

question = "What does SFINAE mean in C++ template metaprogramming?"

print(llm(question))