import json
from flask import Flask
from openai import OpenAI

client = OpenAI()
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "HELLO WORLD FROM AGENTIC AI APP!    "

@app.route('/chatgpt')
def hello_world_chatgpt():
    promt = "you are a 15 year old on crack and sleep deprived, and you are trying to convice your friend why webnovels are PEAK"
    response = client.responses.create(
        model="gpt-5-nano",
        input=promt)
    print(response.output[1].content[0].text)

    text_output = "".join([
        c.text for o in response.output if getattr(o, "content", None)
        for c in o.content if hasattr(c, "text")
    ])
    print(text_output)
    return text_output

if __name__ == '__main__':
    app.run(debug=True)