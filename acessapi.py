secret_key = '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'
prompt = "Tell me what is a situationship"


import openai
openai.api_key = secret_key

output = openai.Completion.create(
    model ='text-curie-001',
    prompt = prompt,
    max_tokens = 300, 
    temperature = 0
)
output_text = output['choices'][0]['text']
print(output_text)