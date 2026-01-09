import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from keep_alive import keep_alive

# ======================
# 讀取環境變數
# ======================
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN_00k")
if not TOKEN:
    raise ValueError("❌ 找不到 DISCORD_TOKEN_00k，請確認 .env 或環境變數")

# ======================
# Bot 設定
# ======================
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="#", intents=intents)

# ======================
# 回覆設定（文字/圖片/GIF）
# ======================
# 統一管理，方便後續新增
RESPONSES_DATA = {
    "鄺玲玲": {"text": "你好", "file": "hello.gif"},

    





    # 可以在這裡繼續新增
    # "關鍵字": {"text": "文字回覆", "file": "檔名.gif 或 png"}
}

WELCOME_CHANNEL_NAME = "歡迎訊息與相關規則🎉"

# ======================
# Bot 上線事件
# ======================
@bot.event
async def on_ready():
    print(f"✅ 機器人已登入 --> {bot.user} (id={getattr(bot.user, 'id', 'Unknown')})")

# ======================

# ======================
# 訊息監聽（文字 + 圖片/GIF）
# ======================
@bot.listen("on_message")
async def remind(message):
    if message.author.bot:
        return

    msg_lower = message.content.lower()
    for key, data in RESPONSES_DATA.items():
        if key in msg_lower:
            text = data.get("text", "")
            file_path = data.get("file")
            if file_path and os.path.exists(file_path):
                await message.channel.send(content=text, file=discord.File(file_path))
            else:
                await message.channel.send(text)
            break

# ======================
# 指令
# ======================
@bot.command(name="鄺玲玲")
async def charsiu_cmd(ctx):
    await ctx.send("我是鄺玲玲")

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention}! 我是鄺玲玲😄")

@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! 🏓 延遲: {round(bot.latency*1000)}ms")

@bot.command()
async def helpme(ctx):
    await ctx.send(
        "指令列表:\n"
        "#鄺玲玲 - 鄺玲玲自我介紹\n"
        "#hello - 打招呼\n"
        "#ping - 測試延遲\n"
    )

# ======================
# 自動重連與啟動
# ======================
def run_bot():
    while True:
        try:
            bot.run(TOKEN)
        except Exception as e:
            print(f"⚠️ Bot 崩潰或斷線，正在重啟... 錯誤: {e}")

if __name__ == "__main__":
    keep_alive()
    run_bot()
