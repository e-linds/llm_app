#this uses the older Chat Completions API, which is supported by Datadog auto-instrumentation
from dotenv import load_dotenv
from openai import OpenAI
from ddtrace.llmobs import LLMObs

load_dotenv()

LLMObs.enable(
    ml_app = "llm_app"
)

client = OpenAI()

def get_response(user_input):

    completion = client.chat.completions.create(
    model="gpt-4.1",
    messages=[
        {"role": "developer", "content": "You are a helpful assistant who gives a maximum of ten-word answers."},
        {"role": "user", "content": f"{user_input}"}
        ]
    )

    response_text = completion.choices[0].message.content

    return response_text