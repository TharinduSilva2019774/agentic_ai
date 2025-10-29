from flask import Flask
from openai import OpenAI

client = OpenAI()
app = Flask(__name__)

@app.route('/')
def hello_world():
    response = client.responses.create(
    model="gpt-5",
    input="Write a one-sentence bedtime story about a unicorn."
)
    return response

if __name__ == '__main__':
    app.run(debug=True)