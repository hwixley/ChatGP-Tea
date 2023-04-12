# ChatGP-Tea CLI ☕️
A CLI for talking to ChatGPT, and turning code blocks (language agnostic) from it's responses into executable shell commands.

## Setup

1. Create an API key on the OpenAI developer portal, and run the following command:
    ```
    export OPENAI_API_KEY=<your-api-key>
    ```

2. Add the `gptea` alias for your script in `.bashrc` (or `.zshrc` for unix) for easy execution in any directory.
   ```
   echo "" >> ~/.bashrc && echo "alias gptea=\"source $(pwd)/gptea.sh\"" >> ~/.bashrc
   ```

3. You are good to go! 🤠 Run `gptea` to get started

## List of commands

1. _ : no input will default to starting a continuous conversation with ChatGPT.
2. `ask` : ask ChatGPT a question without saving any files.
3. `convo` : have a continuous conversation with ChatGPT.
4. `lang <lang-name>` : ask ChatGPT to create a bash script that uses the input language (`<lang-name>`) under the hood.<br>
**Available `<lang-name>` values:**<br>
`python`, `bash`, `javascript`, `typescript`, `java`, `c`, `c++`, `c#`, `rust`, `swift`, `go`, `ruby`, `php`