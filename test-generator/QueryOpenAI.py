from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)




print(completion.choices[0].message.content)
print('model used : ', completion.model)
print(f'Usage : completion tokens {completion.usage.completion_tokens} prompt tokens {completion.usage.prompt_tokens} total tokens {completion.usage.total_tokens}')

with open('test.txt', 'w') as file:
    file.write(str(completion.choices[0].message.content))