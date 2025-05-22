#this uses the older Chat Completions API, which is supported by Datadog auto-instrumentation
from dotenv import load_dotenv
from openai import OpenAI
from ddtrace.llmobs import LLMObs
from ddtrace.llmobs.decorators import llm, task, workflow

load_dotenv()

LLMObs.enable(
    ml_app = "llm_app"
)

client = OpenAI()

# @task
def get_role_desc():
    
    user_input = input('''What is the model's role?
                       ''')
    
    return user_input

# @task
def get_prompt():

    user_input = input('''What would you like to say or ask?
                       ''')
    
    return user_input

# @llm
def get_openai_response(role_desc, prompt):
    

    completion = client.chat.completions.create(
    model="gpt-4.1",
    messages=[
        {"role": "developer", "content": f"{role_desc}. You give a maximum of ten-word answers."},
        {"role": "user", "content": f"{prompt}"}
        ]
    )

    response_text = completion.choices[0].message.content

    return response_text



@workflow
def openai_workflow():

    role_desc = get_role_desc()

    prompt = get_prompt()

    result = get_openai_response(role_desc, prompt)

    return result
