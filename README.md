# Python OS Chatbot

A simple interactive command-line chatbot built with Python that responds to basic conversational prompts in English and Roman Urdu/Hindi, and performs basic file system actions using Python's built-in `os` module.

## Features
- **Conversational Replies:** Responds to greetings (`hello`, `namaste`), check-ins (`how are you`, `kaise ho`), activity questions (`what are you doing`, `kya kar rahe ho`), name questions (`what is your name`, `kya naam hai tumhara`), and mentions of `python` or `weather` / `mausam kaisa hai`.
- **Create a Folder:** Prompts for a folder name and creates it in the current directory using `os.mkdir()`, with error handling if the folder already exists.
- **List Files & Folders:** Displays files and folders in the current working directory using `os.listdir('.')`.
- **Exit Command:** Ends the chat loop cleanly when the user types `exit` or `alvida`.

## Project Structure
- `chatbox.py` — Main Python script containing the interactive chatbot logic.
- `README.md` — Project documentation.

## Requirements
- Python 3.x (uses only the built-in `os` module; no external packages required).

## How to Run
1. Clone or download the repository and open a terminal or VS Code in the project folder.
2. Run the script:
   ```bash
   python chatbox.py
