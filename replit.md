# Discord Bot - 鄺玲玲

## Overview
This is a Discord bot built with discord.py. The bot responds to commands and keywords with text and GIF responses.

## Project Structure
- `00k.py` - Main bot file with commands and event handlers
- `keep_alive.py` - Flask server for keep-alive functionality (runs on port 5000)
- `hello.gif` - GIF file used for responses
- `requirements.txt` - Python dependencies

## Required Environment Variables
- `DISCORD_TOKEN_00k` - Discord bot token (required to run the bot)

## Commands
- `#鄺玲玲` - Bot self-introduction
- `#hello` - Greeting
- `#ping` - Test latency
- `#helpme` - List commands

## Running
The bot runs with `python 00k.py`, which starts:
1. A Flask keep-alive server on port 5000
2. The Discord bot

## Dependencies
- discord.py - Discord API wrapper
- flask - Web framework for keep-alive
- python-dotenv - Environment variable loading
