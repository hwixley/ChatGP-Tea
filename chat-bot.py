import re, os, sys, openai

arg1 = sys.argv[1]
openai.api_key = "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"

def findBash(text):
  matches = re.findall("\`\`\`(bash)*\s((.|\n)*)\s\`\`\`",text)
  # matches is now ['String 1', 'String 2', 'String3']
  return matches

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
    { "role": "user", "content": f"Return just a bash command that can \"{arg1}\". Represent all arguments using the \"$\" prefix and a number to represent the number argument (ie. $1 for the first argument)." },
    ]
)

response = completion.choices[0].message.content
print(response )

bashCommand = response
if "```" in response:
    bashCommand = findBash(response)
    print("OUTPUT:")
    print(bashCommand)


with open('test.sh', 'w') as f:
    f.write(response)
    os.system('chmod +x test.sh')
    os.system('./test.sh potato@gmail.com')
