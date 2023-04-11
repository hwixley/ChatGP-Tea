import openai

class OpenAIService():

    def __init__(self, api_key):
        self.api_key = api_key
        self.engine = "gpt-3.5-turbo"
        self.setup()

    def setup(self):
        openai.api_key = self.api_key

    def get_response(self, prompt):
        message = f"Return a python script that can do the following: \"{prompt}\". Please use backticks (```) to indicate the start and end of the script, and represent all arguments using the \"arg\" prefix and a number to represent the number argument (ie. arg1 for the first argument)."
        completion = openai.ChatCompletion.create(
            model=self.engine,
            messages=[
                {
                    "role": "user",
                    "content": message
                },
            ]
        )

        return completion.choices[0].message.content