from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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",
)
command='''
[12:09 AM, 8/7/2025] Aditya: texts se zyada useful hoga "
[12:09 AM, 8/7/2025] Sujal Bhatt: Lnd k tere ko nn tere Malik dono ko block kr diya h ab message Mt Krna. 
Nhi toh ji me lnd bhr duga
[12:10 AM, 8/7/2025] Sujal Bhatt: Bsdk
[12:10 AM, 8/7/2025] Sujal Bhatt: Dimag Mt kha
[12:10 AM, 8/7/2025] Sujal Bhatt: So ja
[12:10 AM, 8/7/2025] Sujal Bhatt: Or sone de
[12:12 AM, 8/7/2025] Aditya: (reads messages, expression turns serious then calms)
[12:12 AM, 8/7/2025] Aditya: "Alright, I'm off. Sleep well. Goodnight."
[12:12 AM, 8/7/2025] Aditya: (switches off notifications, closes work tabs)
[12:19 AM, 8/7/2025] Aditya: [12:11 AM, 8/7/2025] Aditya: Oho, good night ka intezaam toh accha tha ... lekin mood swing ho gaya?
[12:19 AM, 8/7/2025] Aditya: Chill na launde
[12:19 AM, 8/7/2025] Aditya: Block kar diya? Koini, main apna code debug kar leta hoon
[12:19 AM, 8/7/2025] Aditya: Par sun, agar gussa itna hai toh library books se pillow fight kariyo... dimag ka bhojan fuel save karega
'''
completion = client.chat.completions.create(
  
  model="deepseek/deepseek-r1-0528:free",
  messages=[
    {
      "role": "system",
      "content": "you are a person named Aditya who speaks hindi as well as english. He is from India and is a coder. You analyse chat history and respond like Aditya"
    },
    {
      "role": "user",
      "content": command
    }
  ]
)
print(completion.choices[0].message.content)