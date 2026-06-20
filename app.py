import asyncio
from ollama import AsyncClient


prompt ="""
You are an expert Tech Support.

Give me the specifications of this machine you are installed on in terms of:

JSON Schema:
{
    "type": "array",
    "properties": {
        "os": {"type": "string"},
        "ram": {"type": "string"},
        "gpu": {"type": "string"},
        "cpu": {"type": "string"},
    }
    "required": ["os", "ram", "cpu"]
}
"""

async def chatbot():
    message={'role': 'user', 'content': 'Why is the sky blue?'}
    response = await AsyncClient.chat(
        model='llama3.2',
        messages=[message],
    )
    print(response['message']['content'], end='', flush=True)
        
asyncio.run(chatbot())
    
    








"""in_thinking = False
content = ''
thinking = ''

for chunk in stream:
    if chunk.message.thinking:
        if not in_thinking:
            in_thinking = True
            print('Thinking\n', end='', flush=True)
        print(chunk.message.thinking, end='', flush=True)
        
        # accumulate thinking
        thinking += chunk.message.thinking
    elif chunk.message.content:
        if in_thinking:
            in_thinking = False
            print('\nAnswer\n', end='', flush=True)
        print(chunk.message.content, end='', flush=True)
        
        # accumulate the partial content
        content += chunk.message.content
    
    # append the accumulated chunk
    new_messages = [{'role': 'assistant', thinking: thinking, content: content}]"""

        
