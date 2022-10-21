import openai
import sys
sys.path.append('.lesson')
import openai_functions as gpt3
from colorama import init, Fore, Back, Style
init(autoreset=True)
name="Noah"
print(Fore.BLUE + f"🤖💬 Hello! I'm {name}. I can't wait to work with you!!!!")
print("🧐💬 What should we write a list about?", end="")
chosen_topic = input()
prompt = f"""
I'm a 33-years-old.
Write a essay about {chosen_topic}:
\n
"""
result = gpt3.complete(prompt, max_tokens=1000) 
print()
print()
print(Back.GREEN + "Awesome :) Here's our output:", end="")
print(Fore.GREEN + " " + result)

print(Fore.BLUE + "I ❤️ what we can make together!")