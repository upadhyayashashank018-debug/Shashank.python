
# import os
# import json
# from groq import Groq
# from dotenv import load_dotenv

# # Load API key from .env
# load_dotenv()

# client = Groq(api_key=os.getenv("GROQ_API_KEY"))


# def read_resume(resume_text):
#     prompt = f"""
# You are a resume screening assistant.

# Read the following resume and extract these details:

# 1. Name
# 2. Email
# 3. Years of experience
# 4. Skills

# Then give a candidate score from 0 to 100 based on:
# - Relevant experience
# - Technical skills
# - Overall suitability

# Return ONLY valid JSON in this format:

# {{
#     "name": "",
#     "email": "",
#     "experience": "",
#     "skills": [],
#     "score": 0
# }}

# Resume:
# {resume_text}
# """

#     response = client.chat.completions.create(
#         model="openai/gpt-oss-20b",
#         messages=[
#             {
#                 "role": "user",
#                 "content": prompt
#             }
#         ],
#         temperature=0
#     )

#     return json.loads(response.choices[0].message.content)


# # -------------------------------
# # Resume data
# # -------------------------------

# resumes = [
#     """
#     Rahul Sharma
#     Email: rahul@gmail.com

#     Software Engineer with 4 years of experience.
#     Skills: Python, C++, Java, SQL, Machine Learning, Git.

#     Worked on machine learning applications and backend systems.
#     """,

#     """
#     Priya Kumar
#     Email: priya@gmail.com

#     Computer Science graduate with 2 years of experience.
#     Skills: Python, Java, HTML, CSS, JavaScript, SQL.

#     Worked as a junior software developer.
#     """,

#     """
#     Arjun Reddy
#     Email: arjun@gmail.com

#     AI Engineer with 5 years of experience.
#     Skills: Python, Machine Learning, Deep Learning, TensorFlow,
#     PyTorch, SQL, Docker.

#     Developed AI and machine learning systems.
#     """,

#     """
#     Sneha Rao
#     Email: sneha@gmail.com

#     Software Developer with 3 years of experience.
#     Skills: C++, Java, Python, React, SQL.

#     Developed web applications and software systems.
#     """
# ]


# # -------------------------------
# # Extract information
# # -------------------------------

# candidates = []

# for resume in resumes:
#     try:
#         candidate = read_resume(resume)
#         candidates.append(candidate)

#     except Exception as e:
#         print("Error reading resume:", e)


# # -------------------------------
# # Sort candidates by score
# # -------------------------------

# candidates.sort(
#     key=lambda x: x["score"],
#     reverse=True
# )


# # -------------------------------
# # Get Top 3
# # -------------------------------

# top_3 = candidates[:3]


# # -------------------------------
# # Display results
# # -------------------------------

# print("\n========== TOP 3 CANDIDATES ==========\n")

# for i, candidate in enumerate(top_3, start=1):

#     print(f"Rank {i}")
#     print("Name       :", candidate["name"])
#     print("Email      :", candidate["email"])
#     print("Experience :", candidate["experience"])
#     print("Skills     :", ", ".join(candidate["skills"]))
#     print("Score      :", candidate["score"])
#     print("--------------------------------------")



import os
from time import sleep

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY not found. Add it to your .env file.")

client = Groq(api_key=api_key)
model = "openai/gpt-oss-20b"

JD = """
SQL for querying and managing data
Excel or Google Sheets for organizing and analyzing data
Data visualization tools such as Power BI, Tableau, or Looker
Basic statistics and data analysis
Data cleaning and validation
Familiarity with databases and data warehouses
Python or R for analysis and automation
Reporting and dashboard creation
"""

RESUME = """
Languages: JavaScript, TypeScript, HTML5, CSS3
Frameworks and Libraries: React, Next.js, Vue, Angular, Redux, Tailwind CSS
Tools: Git, GitHub, Vite, Webpack, npm, Figma
Testing: Jest, React Testing Library, Cypress, Playwright
Other: Responsive design, accessibility, REST APIs, performance optimization
"""


def call_llm(system_prompt, user_prompt):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )

    result = response.choices[0].message.content
    print(result)
    return result


def step1():
    system_prompt = (
        "Act as a professional HR assistant. Extract only the skills "
        "explicitly listed in the resume. Do not invent skills."
    )
    user_prompt = f"Extract the skills from this resume:\n{RESUME}"
    return call_llm(system_prompt, user_prompt)


def step2():
    system_prompt = (
        "Act as a professional HR assistant. Extract only the skills "
        "explicitly listed in the job description. Do not invent skills."
    )
    user_prompt = f"Extract the skills from this job description:\n{JD}"
    return call_llm(system_prompt, user_prompt)


def step3(candidate_skills, jd_skills):
    system_prompt = (
        "Compare the candidate's skills with the job description skills. "
        "Do not invent skills. Return a match score out of 100 and a brief "
        "explanation of matching and missing skills."
    )
    user_prompt = f"""
Candidate skills:
{candidate_skills}

Job description skills:
{jd_skills}
"""
    return call_llm(system_prompt, user_prompt)


if __name__ == "__main__":
    candidate_skills = step1()
    sleep(2)

    jd_skills = step2()
    sleep(2)

    score = step3(candidate_skills, jd_skills)