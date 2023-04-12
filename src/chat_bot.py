import os, sys
import openai_service, response_handler, languages

class Main():

    def __init__(self):
        API_KEY = os.environ.get("OPENAI_API_KEY")
        self.openaiService = openai_service.OpenAIService(API_KEY)

    def process_args(self):
        args = sys.argv[1:]
        n = len(args)
        if n > 0:
            arg0 = args[0]
            if arg0 == "ask":
                self.get_response()
            elif arg0 == "lang":
                if n > 1:
                    self.get_lang_response(args[1])
                else:
                    print("\nERROR: No language specified.")
            elif arg0 == "convo":
                self.start_convo()                
            else:
                print(f"\nERROR: Invalid argument: {args[0]}")
        else:
            self.start_convo()

    def start_convo(self):
        print("\nWhat would you like to ask?")
        question = input()

        while question != "exit":
            response = self.openaiService.get_response(question)
            print(f"\nResponse:\n{response}")
            print("\nWhat would you like to ask?")
            question = input()

        print("Would you like to save this conversation? (y/n)")
        save = input()
        if save == "y":
            print("\nWhat would you like to call this conversation?")
            fname = input()
            self.openaiService.save_conversation(fname)
        
        print("\nGoodbye!")

    def get_response(self):
        response = main.ask_question()
        print(f"\nResponse:\n{response}")

    def get_lang_response(self, lang):
        lang = languages.Languages().get_language(lang)
        if lang is not None:
            response = main.ask_lang_question(parseLanguage=lang)
            main.format_lang_response(response, lang=lang)
        else:
            print(f"\nERROR: Invalid language: {lang}")

    def ask_question(self):
        print("\nWhat would you like to ask?")
        question = input()

        return self.openaiService.get_response(question)

    def ask_lang_question(self, parseLanguage=languages.Languages().get_language("python"), executeLanguage="bash"):
        print(f"\nWhat would you like your {executeLanguage} command to do?")
        question = input()

        return self.openaiService.get_lang_response(question, parseLanguage)
    
    def format_lang_response(self, response, lang=languages.Languages().get_language("python")):
        responseHandler = response_handler.ResponseHandler(response)
        code_blocks = responseHandler.findCodeBlocks(lang=lang)

        if len(code_blocks) == 0:
            print("\nERROR: No code found in response.")
            print(f"\nResponse:\n{response}")
            sys.exit()
        else:
            responseHandler.save_code_blocks(code_blocks, lang)
            print(f"\nResponse:\n{response}")


if __name__ == "__main__":
    main = Main()
    main.process_args()