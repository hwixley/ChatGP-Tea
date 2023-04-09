import re, os


with open('test.txt','r') as file:
    test_str = file.read()

def findBash(text):
  matches = re.findall("\`\`\`bash\s((.|\n)*)\s\`\`\`",text)
  return matches

command = findBash(test_str)[0][0]
print(command)

with open('test.sh', 'w') as f:
    f.write(command)

os.system('source test.sh potato@gmail.com')
