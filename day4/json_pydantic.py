
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API KEY NOT FOUND")

client = Groq(api_key=my_api_key)

model = "openai/gpt-oss-20b"
role = "user"
from pydantic import BaseModel
class Ticket(BaseModel):
    name: str
    email: str
    issue: str
schema = Ticket.model_json_schema()
response_format = {
    "type": "json_object"
}
system_prompt = f"""Extract the personal information from ticket stricktly based on this schema{schema} in json format only"""
message_system = {
    "role": "system",
    "content":system_prompt
    }
text = "Hello my name is shashank. My Iphone is not working. My email id is upadhyayashashank018@gmail.com.My phone number is 7019446452"
prompt = f"""This is a customer ticket please extract personal information from {text}"""

message = {"role": role, "content": prompt}
messages = [message_system, message]
    
response = client.chat.completions.create(
    model=model,
    messages=messages,
    response_format=response_format
)
print(response.choices[0].message.content)
