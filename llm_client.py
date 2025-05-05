from dotenv import load_dotenv
from openai import OpenAI
from ddtrace.llmobs import LLMObs

load_dotenv()

LLMObs.enable(
    ml_app = "llm_app"
)

client = OpenAI()

# this uses the openai responses API, which does not appear to be supported for datadog auto instrumentation
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