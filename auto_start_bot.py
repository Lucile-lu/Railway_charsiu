import os
import time
import subprocess
from datetime import datetime

# === 主程式檔案名稱 ===
BOT_FILE = "charsiu_1.py"

# === 錯誤紀錄檔 ===
LOG_FILE = "bot_logs.txt"

def write_log(message):
    """紀錄時間與訊息到 log 檔"""
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}\n")

def run_bot():
    """執行並監控 bot 程式"""
    while True:
        print("🚀 啟動 Discord Bot 中...")
        write_log("🟢 Bot 啟動")

        try:
            process = subprocess.Popen(["python", BOT_FILE])
            process.wait()
        except Exception as e:
            error_msg = f"❌ Bot 執行錯誤：{e}"
            print(error_msg)
            write_log(error_msg)

        print("⚠️ Bot 已中斷，5 秒後重新啟動...")
        write_log("⚠️ Bot 中斷，5 秒後重新啟動")

        time.sleep(5)


if __name__ == "__main__":
    run_bot()
