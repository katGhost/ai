from ollama import Client
from anthropic import Anthropic
import os
import json
import csv

# cient
client = Client()
MODEL_NAME = "llama3.2"

def build_input_prompt(question):
    user_content = f"""
    Please answer the following question:
    <question>{question}</question>
    """
    
    messages = [{"role": "user", "content": user_content}]
    return messages


# Get completions for each ouptput
def get_completions(messages):
    response = client.chat(model=MODEL_NAME, messages=messages, options={"num_predict": 2048})
    return response['message']['content']


# evals -> run evals by category { planning, email, scheduling, prioritisation, summarisation }
def load_eval_file(filename):
    path = os.path.join('assistant', filename)

    with open(path, 'r', encoding="utf-8") as f:
        return [json.loads(line) for line in f]


cases = load_eval_file("planning.jsonl")
# print(type(cases))
# print(cases[1])

# outputs
# outputs = [get_completions(build_input_prompt(question["question"])) for question in cases]

# look at the outputs
# for output, question in zip(outputs, cases, strict=False):
#     print(f"Question: {question['question']}\nGolden Answer: {question['golden_answer']}\nOutput: {output}")


# Save question and golden answer to a .csv for grading.
# Save output to a .txt file
results = []
outputs = []

for case in cases:
    output = get_completions(
        build_input_prompt(case["question"])
    )
    
    results.append({
        "id": case["id"],
        "question": case["question"],
        "golden_answer": case["golden_answer"]
    })
    
    outputs.append({
        "id": case["id"],
        "model_output": output,
    })


# Save to files
def save_to_files():
    os.makedirs('grading/', exist_ok=True)
    # Writing directly to csv
    csv_path = os.path.join('grading', 'human_email.csv')
    with open(csv_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for result in results:
            writer.writerow(result.values())
        csv_file.close()


    # Save Model outputs to a .txt file
    txt_path = os.path.join('grading', 'human_email.txt')
    with open(txt_path, mode='w', encoding='utf-8') as txt_file:
        for model_output in outputs:
            txt_file.write(f"ID: {model_output}\n")


if __name__ == '__main__':
    save_to_files()
