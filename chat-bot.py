import re, os, sys, openai

openai.api_key = "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"

print("\nWhat would you like your bash command to do?")
arg1 = input()

def findBash(text):
  matches = re.findall("\`\`\`(python|bash)*\n((.|\n)*)\`\`\`",text)
  return matches

def findArgs(text):
   matches = re.findall("arg[0-9]",text)
   return matches

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
    { "role": "user", "content": f"Return a python script that can do the following: \"{arg1}\". Represent all arguments using the \"arg\" prefix and a number to represent the number argument (ie. arg1 for the first argument)." },
    ]
)

response = completion.choices[0].message.content

bashCommand = response
if "```" in response:
    bash_code = findBash(response)
    bashCommand = bash_code[0][1]
    print(bash_code)
    print(f"\n{bashCommand}")
else:
    print("\nERROR: No code found in response.")
    print(f"\nResponse:\n{response}")
    sys.exit()

os.sy

print("\nWhat would you like to call your script? (exclude the file extension)")
fname = input()

print(f"\nThis script has {len(findArgs(bashCommand))} arguments.")

fpath = f'generated-scripts/{fname}.py'
with open(fpath, 'w') as f1:
    f1.write(response)
    # os.system(f'chmod +x {fpath}')


bash_fpath = f'generated-scripts/{fname}.sh'
with open(bash_fpath, 'w') as f2:
    f2.write(f"python3 {fpath} $@")
    os.system(f'chmod +x {bash_fpath}')
