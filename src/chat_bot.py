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
            self.save_code_blocks(code_blocks, responseHandler)

    def save_code_blocks(self, code_blocks, responseHandler):
        print("\nWhat would you like to call your script? (exclude the file extension)")
        fname = input()

        num_args = len(responseHandler.findArgs())
        print(f"\nThis script has {num_args} arguments.")

        dirpath = f'generated-scripts/{fname}'
        os.system(dirpath)

        file_paths = []
        for i, code_block in enumerate(code_blocks):
            file_paths += [f'{dirpath}/{fname}-{i}.py']
            self.save_file(file_paths[-1], code_block[1])

        self.save_file(f'{dirpath}/{fname}.sh', f"python3 {file_paths[0]} $@")

    def save_file(self, file_path, file_content):
        with open(file_path, 'w') as f:
            f.write(file_content)
            if file_path.endswith(".sh"):
                os.system(f'chmod +x {file_path}')

if __name__ == "__main__":
    main = Main()
    response = main.ask_question()
    main.format_response(response)