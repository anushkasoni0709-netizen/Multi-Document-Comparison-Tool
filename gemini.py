import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

def generate_summary(text):

    prompt = f"""
Read the following documents.

Generate:

1. Overall Summary
2. Key Points
3. Important Topics

{text}
"""

    response = client.chat.completions.create(
        model="meta-llama/llama-3.3-70b-instruct",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content

def compare_documents(text):
    prompt = f"""
You are an AI document comparison assistant.

Compare the uploaded documents and provide:

1. Overall Comparison
2. Similarities
3. Differences
4. Common Topics
5. Unique Information in each document
6. Final Conclusion

Documents:

{text}
"""

    response = client.chat.completions.create(
        model="meta-llama/llama-3.3-70b-instruct",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content
def calculate_similarity(text):

    prompt = f"""
You are an AI document analysis expert.

Read the uploaded documents carefully.

Return ONLY one similarity percentage between 0 and 100.

Example:
87

Documents:

{text}
"""

    response = client.chat.completions.create(
        model="meta-llama/llama-3.3-70b-instruct",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content.strip()