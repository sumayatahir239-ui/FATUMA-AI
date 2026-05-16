# FATUMA AI

FATUMA AI is a simple Python chatbot application built with the Groq API and LangChain. It uses environment variables to securely load your Groq API key and provides an interactive command line interface for conversational AI.

## Project Overview

- `agent.py` is the main script.
- The app loads `GROQ_API_KEY` from a `.env` file using `python-dotenv`.
- It creates a `ChatGroq` chatbot using the `llama-3.3-70b-versatile` model.
- The conversation is managed with `SystemMessage`, `HumanMessage`, and `AIMessage` from `langchain_core.messages`.
- Users can chat in the terminal and type `exit` to quit.

## Features

- Secure API key loading from `.env`
- Simple terminal-based chat loop
- Persistent conversation history during a session
- Uses a custom system prompt identifying the bot as FATUMA

## Requirements

- Python 3.10+ (recommended)
- `python-dotenv`
- `langchain-groq`
- `langchain-core`

## Setup

1. Create a `.env` file in the project directory.
2. Add your Groq API key:

```env
GROQ_API_KEY=your_api_key_here
```

3. Install dependencies:

```bash
pip install python-dotenv langchain-groq langchain-core
```

## Usage

Run the chatbot with:

```bash
python agent.py
```

Then type a message and press Enter. Type `exit` to end the session.

## Notes

- The script uses a fixed system prompt, but you can customize `system_prompt` in `agent.py`.
- Conversation history is kept in memory only while the script is running.
