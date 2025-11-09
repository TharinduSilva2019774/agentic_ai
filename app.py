from flask import Flask, render_template, request
import openai 

client = openai.OpenAI()
app = Flask(__name__)

def get_completion(system_prompt, prompt, model="gpt-5-nano"):
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
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
    system_prompt = "You are a reasecher AI assistant that helps with research tasks. You write 500 word detailed answers."
    model = "gpt-4.1"
    if request.method == 'POST':
        prompt = request.form.get('prompt', '').strip()
        if prompt:
            try:
                result_prv = get_completion(system_prompt, prompt, model)
                word_count = len(result_prv.split())
                write_to_journal = f"""############################################################
Model used: {model}
                
System_prompt: {system_prompt}

User_Prompt: {prompt}

Response: {result_prv}

word_count: {word_count}

############################################################"""
# Removed temporarily for being too costly                
#                 iteration = 0
#                 word_diff = abs(word_count - 500)
#                 print(word_diff)
#                 while (word_diff > 10) and iteration < 5:
#                     new_promt = f"""The previous response you provided was {word_diff} words long. Please rewrite your previous response to be exactly 500 words. There is the previous response for reference: {result_prv}"""
#                     result_prv = get_completion(system_prompt, new_promt, model)
#                     word_count = len(result_prv.split())
#                     iteration += 1
#                     write_to_journal = f"""############################################################
# Model used: {model}
                
# System_prompt: {system_prompt}

# User_Prompt: {new_promt}

# Response: {result_prv}

# word_count: {word_count}

# iteration: {iteration}
# ############################################################"""
#                     write_to_file('journal.txt', write_to_journal)


                result = result_prv
                
                write_to_file('journal.txt', write_to_journal)
            except Exception as exc:
                error = f"Something went wrong: {exc}"
        else:
            error = "Prompt is required."

    return render_template('index.html', prompt=prompt, result=result, error=error)

if __name__ == '__main__':
    app.run(debug=True)


