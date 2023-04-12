import re, os
import languages

class ResponseHandler():
        
    def __init__(self, response):
        self.response = response

    def regexString(self, str):
        return str.replace("+","\+")

    def findCodeBlocks(self, lang=languages.Languages().get_language("python")):
        cb_regex = f"\`\`\`({self.regexString(lang.name)})*\n((.|\n)*)\`\`\`"
        return re.findall(cb_regex, self.response)
    
    def findArgs(self):
        args_regex = "arg[0-9]"
        return re.findall(args_regex, self.response)

    def save_code_blocks(self, code_blocks, lang=languages.Languages().get_language("python")):
        print("\nWhat would you like to call your script? (exclude the file extension)")
        fname = input()

        num_args = len(self.findArgs())
        print(f"\nThis script has {num_args} arguments.")

        dirpath = f'generated-scripts/{fname}'
        os.system(f"mkdir {dirpath}")

        file_paths = []
        for i, code_block in enumerate(code_blocks):
            file_paths += [f'{dirpath}/{fname}_cb{i}.{lang.extension}']
            self.save_file(file_paths[-1], code_block[1])

        self.save_file(f'{dirpath}/{fname}.sh', f"{lang.command} {file_paths[0]} $@")

    def save_file(self, file_path, file_content):
        with open(file_path, 'w') as f:
            f.write(file_content)
            if file_path.endswith(".sh"):
                os.system(f'chmod +x {file_path}')