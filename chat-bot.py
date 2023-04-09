import re, os, sys, openai

openai.api_key = "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"

print("What would you like your bash command to do?")
arg1 = input()

def findBash(text):
  matches = re.findall("\`\`\`((.|\n)*)\`\`\`",text)
  return matches

def findArgs(text):
   matches = re.findall("\$[0-9]",text)
   return matches

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
    { "role": "user", "content": f"Return a bash script that can do the following: \"{arg1}\". Represent all arguments using the \"$\" prefix and a number to represent the number argument (ie. $1 for the first argument)." },
    ]
)

response = completion.choices[0].message.content

bashCommand = response
if "```" in response:
    bashCommand = findBash(response)[0][1]

print("What would you like to call your script? (exclude the .sh extension)")
fname = input()

print(f"This script has {len(findArgs(bashCommand))} arguments.")

with open(f'{fname}.sh', 'w') as f:
    f.write(response)
    os.system('chmod +x test.sh')
    # os.system('./test.sh potato@gmail.com')
