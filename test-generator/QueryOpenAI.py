from openai import OpenAI
client = OpenAI()
file_contents = ""
with open('test-prompt.txt','r') as file:
    file_contents = file.read()

print(file_contents)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo-0125",
  messages=[
    {"role": "system", "content": ""},
    {"role": "user", "content": file_contents}
  ]
)




print(completion.choices[0].message.content)
print('model used : ', completion.model)
print(f'Usage : completion tokens {completion.usage.completion_tokens} prompt tokens {completion.usage.prompt_tokens} total tokens {completion.usage.total_tokens}')

with open('test.txt', 'w') as file:
    file.write(str(completion.choices[0].message.content))