import os
from google import genai
from dotenv import load_dotenv
from ddtrace.llmobs import LLMObs
from ddtrace.llmobs.decorators import llm, task, workflow

load_dotenv()

LLMObs.enable(
    ml_app = "llm_app"
)

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])


def get_prompt():

    user_input = input('''What would you like to say or ask?
                       ''')
    
    return user_input


def get_gemini_response(prompt):

    response = client.models.generate_content(
    model="gemini-2.0-flash", contents=f"In ten words or fewer: {prompt}"
    )

    return response.text


def gemini_workflow():

    prompt = get_prompt()

    result = get_gemini_response(prompt)

    return result

