import re, os

class ResponseHandler():
        
    def __init__(self, response):
        self.response = response

    def findCodeBlocks(self):
        cb_regex = "\`\`\`(python|bash)*\n((.|\n)*)\`\`\`"
        return re.findall(cb_regex, self.response)
    
    def findArgs(self):
        args_regex = "arg[0-9]"
        return re.findall(args_regex, self.response)

    def save_code_blocks(self, code_blocks):
        print("\nWhat would you like to call your script? (exclude the file extension)")
        fname = input()

        num_args = len(self.findArgs())
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