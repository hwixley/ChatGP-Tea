# ChatGP-Tea CLI ☕️
A CLI for talking to ChatGPT:, saving conversation logs, and turning code blocks (language agnostic) from it's responses into executable shell commands.

![Screenshot from 2023-04-22 19-56-19](https://user-images.githubusercontent.com/57837950/233849218-76dc5242-1fac-4886-b6f5-86f98d0e5165.png)

## Setup

1. Install the python dependencies:
    ```
    pip install -r requirements.txt
    ```

2. Create an API key on the OpenAI developer portal.
3. Replace `YOUR_API_KEY` in the `.env` file with your OpenAI API key.
    <br>OR<br>
    You can run the following command: (however this does not get persisted on reboot)
    ```
    export OPENAI_API_KEY=<your-api-key>
    ```

4. Run the setup script. This will add the `gptea` alias for your script in `.bashrc` for easy execution in any directory, and add local directories (`generated-scripts/` and `conversations/`) for saving ChatGPT: generated files or conversations.
   ```
   chmod +x setup.sh && source setup.sh
   ```

5. You are good to go! 🤠 Run `gptea` to get started.

## List of commands

1. _ : no input will display the list of commands.
2. `ask` : ask ChatGPT: a question without saving any files.
3. `convo` : have a continuous conversation with ChatGPT:.
4. `lang <lang-name>` : ask ChatGPT: to create a bash script that uses the input language (`<lang-name>`) under the hood.<br>
**Available `<lang-name>` values:**<br>
`python`, `bash`, `javascript`, `typescript`, `java`, `c`, `c++`, `c#`, `rust`, `swift`, `go`, `ruby`, `php`
