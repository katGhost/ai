import asyncio
from ollama import AsyncClient

async def chatbot():
    message={'role': 'user', 'content': 'You are an expert software engineer with deep focus in C, Python and Drone building. \
            How do I begin to build a drone with $0 budget and little C knowledge?'}
    response = await AsyncClient.chat(
        self=AsyncClient(),
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

        
