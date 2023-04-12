# ChatGPTea CLI ☕️
A CLI for talking to ChatGPT, and turning code blocks from it's responses into executable shell commands.

## Setup

1. Create an API key on the openai developer portal, and run the following command:
    ```
    export OPENAI_API_KEY=<your-api-key>
    ```

2. Add the `gptea` alias for your script in `.bashrc` (or `.zshrc` for unix) for easy execution in any directory.
   ```
   echo "" >> ~/.bashrc && echo "alias gptea=\"source $(pwd)/chatBot.sh\"" >> ~/.bashrc
   ```

3. You are good to go! :)