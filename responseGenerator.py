import openai
from dotenv import dotenv_values
from promptColor import get_and_render_colors

config = dotenv_values(".env")
openai.api_key = config["OPENAI_KEY"]

def response_gen():
    prompt = get_and_render_colors(input("Give a description for a desired color palette: "))
    response = openai.Completion.create(
        prompt=prompt,
        model="gpt-3.5-turbo-instruct",
        max_tokens=200,
        stop="11."
    )
    return response['choices'][0]['text']

