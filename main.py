from openai import OpenAI

openai = OpenAI(api_key='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')

user_input = input("Ingresa tu mensaje: ")

response = openai.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_input}
    ],
    temperature=1,
    max_tokens=100,
    top_p=1,
    frequency_penalty=0.5,
    presence_penalty=0
)

response.choices[0].message
print(response)