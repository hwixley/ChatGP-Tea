import re
import os


with open('test.txt','r') as file:
    test_str = file.read()
# print(countriesStr)
 
# print("hello")
# test_str = """"""
# print(test_str)

def findBash(text):
  matches = re.findall("\`\`\`bash\s((.|\n)*)\s\`\`\`",text)
  # matches is now ['String 1', 'String 2', 'String3']
  return matches

command = findBash(test_str)[0][0]
print(command)

with open('test.sh', 'w') as f:
    f.write(command)

os.system('source test.sh potato@gmail.com')
