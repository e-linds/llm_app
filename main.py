
from llm_client import get_response

def app():

   input_var = input('''What is your question? 
              ''')
   answer = get_response(input_var)

   print(answer)



if __name__ == "__main__":
    app()
