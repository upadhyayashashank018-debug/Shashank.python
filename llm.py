
import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def read_resume(resume_text):
    prompt = f"""
You are a resume screening assistant.

Read the following resume and extract these details:

1. Name
2. Email
3. Years of experience
4. Skills

Then give a candidate score from 0 to 100 based on:
- Relevant experience
- Technical skills
- Overall suitability

Return ONLY valid JSON in this format:

{{
    "name": "",
    "email": "",
    "experience": "",
    "skills": [],
    "score": 0
}}

Resume:
{resume_text}
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    return json.loads(response.choices[0].message.content)


resumes = [
    """
    Rahul Sharma
    Email: rahul@gmail.com

    Software Engineer with 4 years of experience.
    Skills: Python, C++, Java, SQL, Machine Learning, Git.

    Worked on machine learning applications and backend systems.
    """,

    """
    Priya Kumar
    Email: priya@gmail.com

    Computer Science graduate with 2 years of experience.
    Skills: Python, Java, HTML, CSS, JavaScript, SQL.

    Worked as a junior software developer.
    """,

    """
    Arjun Reddy
    Email: arjun@gmail.com

    AI Engineer with 5 years of experience.
    Skills: Python, Machine Learning, Deep Learning, TensorFlow,
    PyTorch, SQL, Docker.

    Developed AI and machine learning systems.
    """,

    """
    Sneha Rao
    Email: sneha@gmail.com

    Software Developer with 3 years of experience.
    Skills: C++, Java, Python, React, SQL.

    Developed web applications and software systems.
    """
]


candidates = []
