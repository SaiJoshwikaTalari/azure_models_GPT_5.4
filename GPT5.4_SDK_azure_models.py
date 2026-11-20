from openai import OpenAI
    
endpoint ="https://project123456.services.ai.azure.com/openai/v1"
deployment_name = "gpt-5.4-mini"
api_key = "7z3sQhR15CLCTB4cAyresbikh7nwO7JQQJ99CKACF24PCXJ3w3AAAAACOGAjfB"
    
client = OpenAI(
     base_url=endpoint,
     api_key=api_key
 )
    
response = client.responses.create(
     model=deployment_name,
     input=[{
         "role": "user",
         "content": [
             {"type": "input_text", "text": "what's in this image?"},
             {"type": "input_image", "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSopLhoZOZ7-ROTmYHFiKfiS1B_G8MeWXeDzgDDWeNI0A&s=10"},
         ],
     }],
 )
    
print(f"answer: {response.output_text}")
