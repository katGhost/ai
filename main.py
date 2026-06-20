from ollama import chat
import os

# read from file, read content
def read_content():
    path = os.path.join('xml', 'reminder.xml')
    
    with open(path, 'r', encoding="utf-8") as f:
        return f.read()

def summarize(xml_content):
    """Model responses -> prompt engineering happens below"""
    response = chat(
        model='llama3.2',
        messages=[
            {
                "role": "system",
                "content": "You are a personal assistant."
            },
            {
                "role": "user",
                "content": xml_content
            }
        ],
        # think='medium',
        stream=False,
        options={
            "temperature": 0.7,
            "num_predict": 512,
        },
    )
    
    return response.message.content

def save_response(content):
    """write to file in files/, save the response from the llm"""
    os.makedirs('files/', exist_ok=True)
    
    output_path = os.path.join('files', 'reminder.txt')
    
    with open(output_path, 'w', encoding="utf-8") as f:
        f.write(content)

def main():
    xml_content = read_content()
    
    response_text = summarize(xml_content)
    
    save_response(response_text)


if __name__ == "__main__":
    main()
