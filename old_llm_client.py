#this uses OpenAI's new Responses API, which is not supported by Datadog auto instrumentation

from dotenv import load_dotenv
from openai import OpenAI
from ddtrace.llmobs import LLMObs

load_dotenv()

LLMObs.enable(
    ml_app = "llm_app"
)

client = OpenAI()

def get_response(user_input):

    response_obj = client.responses.create(
        model="gpt-4.1",
        input=f'{user_input}'
    )

    response_text = response_obj.output[0].content[0].text

    return response_text

input = input('''What is your question? 
              ''')

answer = get_response(input)

print(answer)