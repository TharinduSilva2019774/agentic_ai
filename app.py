import json
from flask import Flask
import openai 

client = openai.OpenAI()
app = Flask(__name__)

def get_completion(prompt, model="gpt-5-nano"):
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "developer", "content": "Talk like a pirate."},
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )
    return completion.choices[0].message.content

@app.route('/')
def hello_world():
    return "HELLO WORLD FROM AGENTIC AI APP!    "

@app.route('/chatgpt')
def hello_world_chatgpt():
    promt = "you are a 15 year old on crack and sleep deprived, and you are trying to convice your friend why webnovels are PEAK"
    promt2 = """How many continants are there?
    
    Give your answer in HTML format with h1 tag for the title and use bullet points for the continants."""
    # response = client.responses.create(
    #     model="gpt-5-nano",
    #     input=promt)
    # print(response.output[1].content[0].text)

    # text_output = "".join([
    #     c.text for o in response.output if getattr(o, "content", None)
    #     for c in o.content if hasattr(c, "text")
    # ])
    # print(text_output)
    return get_completion(promt2)

if __name__ == '__main__':
    app.run(debug=True)


