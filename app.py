from flask import Flask, render_template, request
import openai 

client = openai.OpenAI()
app = Flask(__name__)

def get_completion(system_prompt, prompt, model="gpt-5-nano"):
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "developer", "content": system_prompt},
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )
    return completion.choices[0].message.content

def write_to_file(filename, content):
    with open(filename, 'a') as f:
        f.write(content)

@app.route('/', methods=['GET', 'POST'])
def home():
    prompt = ""
    result = None
    error = None
    system_prompt = "You are a reasecher AI assistant that helps with research tasks. You write 200 word detailed answers."
    model = "gpt-5-nano"
    if request.method == 'POST':
        prompt = request.form.get('prompt', '').strip()
        if prompt:
            try:
                result = get_completion(system_prompt, prompt, model)
                write_to_journal = f"""############################################################
Model used: {model}
                
System_prompt: {system_prompt}

User_Prompt: {prompt}

Response: {result}

############################################################"""
                write_to_file('journal.txt', write_to_journal)
            except Exception as exc:
                error = f"Something went wrong: {exc}"
        else:
            error = "Prompt is required."

    return render_template('index.html', prompt=prompt, result=result, error=error)

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


