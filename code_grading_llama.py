from ollama import Client
from anthropic import Anthropic
import os

# client = Anthropic(
#     base_url='http://localhost:11434/',
#     api_key='ollama'
# )
client = Client()
MODEL_NAME = "llama3.2"

# Define input prompt template for the task
def build_input_prompt(animal_statement):
    """Find out how many legs an animal has"""
    user_content = f"""
    You will be provided a statement about an animal and your job is to determine how many legs that animal has.
    
    Here is the animal statement:
    <animal_statement>{animal_statement}</animal_statement>
    
    How many legs does the animal have? Return just the number of legs as an integer and nothing else.
    """
    
    messages = [{"role": "user", "content": user_content}]
    return messages


# Define our eval -> doing this in jsonl file later, or CSV
eval = [
    {"animal_statement": "The animal is a human.", "golden_answer": "2"},
    {"animal_statement": "The animal is a snake.", "golden_answer": "0"},
    {
        "animal_statement": "The fox lost a leg, but then magically grew back the leg he lost and a mysterious extra leg on top of that.",
        "golden_answer": "5",
    },
]

# get completions for each input -> with Anthropic
"""def get_completions(messages):
    response = client.messages.create(model=MODEL_NAME, messages=messages, max_tokens=5)
    return response.content[0].text"""

# get completions for each input -> With Ollama
def get_completions(messages):
    response = client.chat(model=MODEL_NAME, messages=messages, options={"num_predict": 5})
    return response['message']['content']

# Get completions for each question in the evals
outputs = [get_completions(build_input_prompt(question["animal_statement"])) for question in eval]

# get all outputs in a list -> solving an issue with saving ot a .txt file
all_outputs = []

# get the outputs
for output, question in zip(outputs, eval, strict=False):
    all_outputs.append(
        f"Animal Statement: {question["animal_statement"]}\n"
        f"Golden Answer: {question["golden_answer"]}\n"
        f"Output: {output}\n"
    )

output_result = "\n".join(all_outputs)


# Check our completions against the goldern answers
# define a grader function
def grade_completions(output, golden_answer):
    return output == golden_answer

grades = [
    grade_completions(output, question["golden_answer"]) for output, question in zip(outputs, eval, strict=False)
]

score = sum(grades) / len(grades) * 100
# print(f"Score: {score:.2f}%")

# Save outputs and score to a .txt file
def save_output_score():
    os.makedirs('files/', exist_ok=True)

    output_path = os.path.join('files', 'code_grading.txt')
    
    with open(output_path, 'w', encoding="utf-8") as f:
        f.write(f"Outputs\n{output_result}\n\nGrading Score\nActual Score: {score}%\nRounded Score: {score:.2f}%")

save_output_score()

