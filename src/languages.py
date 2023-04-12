
class Language():

    def __init__(self, name, command, extension):
        self.name = name
        self.command = command
        self.extension = extension

class Languages():
    languages = [
        Language("python", "python3", "py"),
        Language("bash", "bash", "sh"),
        Language("javascript", "node", "js"),
        Language("java", "java", "java"),
        Language("c", "gcc", "c"),
        Language("c++", "g++", "cpp"),
        Language("c#", "csc", "cs"),
        Language("go", "go run", "go"),
        Language("php", "php", "php"),
        Language("ruby", "ruby", "rb"),
        Language("rust", "rustc", "rs"),
        Language("swift", "swift", "swift"),
        Language("typescript", "ts-node", "ts"),
    ]

    def get_language(self, name):
        for language in self.languages:
            if language.name == name:
                return language
        return None