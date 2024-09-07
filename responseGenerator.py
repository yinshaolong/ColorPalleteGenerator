# import openai
import json
from dotenv import load_dotenv
import openai
import os
import argparse

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI()

# def get_prompt():
#     with open("promptColor.json") as f:
#         return json.load(f)
    

def response_gen(query):
    # prompt = get_prompt()
    # query = {"role" : "user", "content":f'Convert the following verbal description of a color palette into a list of colors: {query}'}
    # prompt.append(query)
    # print(type(prompt), prompt)
    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages = [
    {"role": "system", "content": "You are a color palette generating assistant that responds to text prompts for color palettes. You should generate color palettes that fit the theme, mood, or instructions in the prompt. The palettes should be between 2 and 8 colors."},
    {"role": "user", "content": "Convert the following verbal description of a color palette into a list of colors: The Mediterranean Sea"},
    {"role": "assistant", "content": '["#006699", "#66CCCC", "#F0E68C", "#008000", "#F08080"]'},
    {"role": "user", "content": "Convert the following verbal description of a color palette into a list of colors: sage, nature, earth"},
    {"role": "assistant", "content": '["#EDF1D6", "#9DC08B", "#609966", "#40513B"]'},
    {"role": "user", "content": "Convert the following verbal description of a color palette into a list of colors:"},
    {"role" : "user", "content":f'Convert the following verbal description of a color palette into a list of colors: {query}'},
]
    )
    return json.loads(response.choices[0].message.content)
def main():
    query = input("Enter a prompt to generate a color: ")
    print(response_gen(query))
if __name__ == "__main__":
     main()