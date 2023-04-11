import os, sys
import openai_service, response_handler

class Main():

    def __init__(self):
        API_KEY = os.environ.get("OPENAI_API_KEY")
        self.openaiService = openai_service.OpenAIService(API_KEY)

    def ask_question(self):
        print("\nWhat would you like your bash command to do?")
        question = input()

        return self.openaiService.get_response(question)
    
    def format_response(self, response):
        responseHandler = response_handler.ResponseHandler(response)

        code_blocks = responseHandler.findCodeBlocks()

        if len(code_blocks) == 0:
            print("\nERROR: No code found in response.")
            print(f"\nResponse:\n{response}")
            sys.exit()
        else:
            responseHandler.save_code_blocks(code_blocks)
            print(f"\nResponse:\n{response}")


if __name__ == "__main__":
    main = Main()
    response = main.ask_question()
    main.format_response(response)