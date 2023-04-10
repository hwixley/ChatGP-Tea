import openai

class OpenAIService():

    def __init__(self, api_key):
        self.api_key = api_key
        self.setup()

    def setup(self):
        openai.api_key = self.api_key

    def get_response(self, prompt):
        # completion = openai.Completion.create(
        #     engine="davinci",
        #     prompt=prompt,
        #     temperature=0.9,
        #     max_tokens=150,
        #     top_p=1,
        #     frequency_penalty=0,
        #     presence_penalty=0,
        #     stop=["\n", " Human:", " AI:"]
        # )
        # return completion.choices[0].text

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                },
            ]
        )

        return completion.choices[0].message.content