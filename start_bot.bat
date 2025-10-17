@echo off
title Discord Bot 自動重啟系統
echo =====================================
echo 🚀 正在啟動 Discord Bot 自動守護程式...
echo =====================================

call venv\Scripts\activate
python auto_start_bot.py
pause
