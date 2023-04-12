# ChatGP-Tea CLI ☕️
A CLI for talking to ChatGPT, saving conversation logs, and turning code blocks (language agnostic) from it's responses into executable shell commands.

## Setup

1. Create an API key on the OpenAI developer portal, and run the following command:
    ```
    export OPENAI_API_KEY=<your-api-key>
    ```

2. Run the setup script. This will add the `gptea` alias for your script in `.bashrc` for easy execution in any directory, and add local directories (`generated-scripts/` and `conversations/`) for saving ChatGPT generated files or conversations.
   ```
   chmod +x setup.sh && source setup.sh
   ```

3. You are good to go! 🤠 Run `gptea` to get started

## List of commands

1. _ : no input will default to starting a continuous conversation with ChatGPT.
2. `ask` : ask ChatGPT a question without saving any files.
3. `convo` : have a continuous conversation with ChatGPT.
4. `lang <lang-name>` : ask ChatGPT to create a bash script that uses the input language (`<lang-name>`) under the hood.<br>
**Available `<lang-name>` values:**<br>
`python`, `bash`, `javascript`, `typescript`, `java`, `c`, `c++`, `c#`, `rust`, `swift`, `go`, `ruby`, `php`