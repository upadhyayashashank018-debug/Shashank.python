# # # # import os
# # # # from dotenv import load_dotenv
# # # # from groq import Groq

# # # # load_dotenv()

# # # # my_api_key = os.getenv("GROQ_API_KEY")

# # # # if not my_api_key:
# # # #     raise ValueError("API KEY NOT FOUND")

# # # # client = Groq(api_key=my_api_key)

# # # # model = "openai/gpt-oss-20b"

# # messages = [
# #     {
# #         "role": "user",
# #         "content": "Do you know Virat Kohli?"
# #     }
# # ]

# # response = client.chat.completions.create(
# #     model=model,
# #     messages=messages
# # )

# # print(response.choices[0].message.content)

# # # ## Day 2 temperature and system role

# # # import os
# # # from dotenv import load_dotenv
# # # from groq import Groq

# # # load_dotenv()

# # # my_api_key = os.getenv("GROQ_API_KEY")

# # # if not my_api_key:
# # #     raise ValueError("API KEY NOT FOUND")

# # # client = Groq(api_key=my_api_key)

# # # model = "openai/gpt-oss-20b"
# # # role = "user"
# # # prompt  = "I love You"
# # # message1 = {
# # #     "role": "system",
# # #     "content": "Act like mother and reply ",
# # # }
# # # message = {"role": role, "content": prompt}
# # # messages = [message1, message]

# # # response = client.chat.completions.create(
# # #     model=model,
# # #     messages=messages
# # # )

# # # print(response.choices[0].message.content)

# # #Day3 : Tokens

# # import os
# # from dotenv import load_dotenv
# # from groq import Groq

# # load_dotenv()

# # my_api_key = os.getenv("GROQ_API_KEY")

# # if not my_api_key:
# #     raise ValueError("API KEY NOT FOUND")

# # client = Groq(api_key=my_api_key)

# # model = "openai/gpt-oss-20b"
# # role = "user"
# # prompt1  = "Hi"
# # prompt2 = "Explain football in detail"
# # prompt3 = "Write essay about pollution in 1000 words"
# # prompts = [prompt1, prompt2, prompt3]
# # for prompt in prompts:
# #     message = {"role": role, "content": prompt}
# #     messages = [message]
    
# #     response = client.chat.completions.create(
# #     model=model,
# #     messages=messages
# # )
# #     usage = response.usage
# #     print(f"Prompt: {prompt} --->your tokens: {usage.prompt_tokens} --->response tokens: {usage.completion_tokens} --->Total tokens = {usage.prompt_tokens}+{usage.completion_tokens}")
















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
