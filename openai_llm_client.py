#this uses the older Chat Completions API, which is supported by Datadog auto-instrumentation
from dotenv import load_dotenv
from openai import OpenAI
from ddtrace.llmobs import LLMObs

load_dotenv()

LLMObs.enable(
    ml_app = "llm_app"
)

client = OpenAI()

def get_openai_response():
    
    model_role_desc = input('''Describe the role. 
              ''')
    
    question = input('''What is your question? 
              ''')
    

    completion = client.chat.completions.create(
    model="gpt-4.1",
    messages=[
        {"role": "developer", "content": f"{model_role_desc}. You give a maximum of ten-word answers."},
        {"role": "user", "content": f"{question}"}
        ]
    )

    response_text = completion.choices[0].message.content

    return response_text