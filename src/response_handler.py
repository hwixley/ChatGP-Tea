import re

class ResponseHandler():
        
    def __init__(self, response):
        self.response = response

    def findCodeBlocks(self):
        cb_regex = "\`\`\`(python|bash)*\n((.|\n)*)\`\`\`"
        return re.findall(cb_regex, self.response)
    
    def findArgs(self):
        args_regex = "arg[0-9]"
        return re.findall(args_regex, self.response)
