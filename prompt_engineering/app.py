from ollama import chat
import os

response = chat(
    model='llama3.2',
    messages=[
        {
            "role": "user",
            "content": "."
        }
    ],
    # think='medium',
    stream=False,
    options={
        "temperature": 0.7,
        "num_predict": 512,
    },
)


# write to a file instead
with open('responses.txt', 'w', encoding="utf-8") as f:
    f.write(response.message.content)
