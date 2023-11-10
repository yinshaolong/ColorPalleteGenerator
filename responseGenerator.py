import openai
from dotenv import dotenv_values

config = dotenv_values(".env")
openai.api_key = config["OPENAI_KEY"]

def responseGen(prompt):
    prompt = f'{prompt} Text: {input("Prompt: ")} Result:'
    response = openai.Completion.create(
        prompt=prompt,
        model="gpt-3.5-turbo-instruct",
        max_tokens=200,
        stop="11."
    )
    return response['choices'][0]['text']

