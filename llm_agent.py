import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_response(query, context_chunks):

    context = "\n\n".join(context_chunks)

    system_prompt = """
You are an ATS Resume Matching Engine.

Return ONLY this format:

Match Score: <number>%

Strong Areas:
- Skill 1
- Skill 2

Missing Skills:
- Skill 1
- Skill 2

ATS Score: <number>/100

Suggested Summary:
<Rewrite summary>
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",   # ✅ working model
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Resume + JD:\n{context}\n\nQuestion:{query}"}
        ],
        temperature=0.2,
        max_tokens=800
    )

    return response.choices[0].message.content