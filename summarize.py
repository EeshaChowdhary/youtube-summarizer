from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def summarize(transcript):
    words = transcript.split()
    trimmed = " ".join(words[:5000])

    prompt = f"""
    You are an expert note-taker and educator. Based on this YouTube transcript, give me a DETAILED output:

    1. **Key Takeaways** - 10 detailed bullet points, each 2-3 sentences long
    2. **Detailed Notes** - Section wise notes like a student would write, with subpoints
    3. **Blog Post Summary** - 300 words, engaging and informative
    4. **Important Terms** - 8 terms with clear, simple explanations
    5. **What You Should Do Next** - 3 action items based on what was taught

    Be thorough and detailed. Don't be brief.

    Transcript: {trimmed}
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content