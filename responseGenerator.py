import openai
from dotenv import dotenv_values
from promptColor import get_and_render_colors
import json

config = dotenv_values(".env")
openai.api_key = config["OPENAI_KEY"]

def response_gen(query):
    prompt = get_and_render_colors(query)
    response = openai.completions.create(
        prompt=prompt,
        model="gpt-3.5-turbo-instruct",
        max_tokens=200,
        stop="11."
    )
    # return json.loads(response['choices'[0]['text'])

    #Completion is a dictionary. Choices is a dictionary with a list as an object. The first index of the list is a dictionary with text as a key. 
    return json.loads(response.choices[0].text)

def main():
    query = input("Enter a color: ")
    print(response_gen(query))
if __name__ == "__main__":
    main()