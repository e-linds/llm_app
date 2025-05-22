
from openai_llm_client import openai_workflow
from gemini_llm_client import gemini_workflow

def app():

  library = input('''What library would you like to use? OpenAI (1), Gemini (2)
                  ''')
  
  if library == "1":

    result = openai_workflow()
  
  elif library == "2":
     
    result = gemini_workflow()

  else:
     print("That's not an option")
     return

  print(result)


if __name__ == "__main__":
    app()
