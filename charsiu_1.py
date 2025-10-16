import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from keep_alive import keep_alive

load_dotenv()  # ← 這行一定要有！


# ======================
# 讀取 Token（從環境變數）
# ======================
TOKEN = os.getenv("DISCORD_TOKEN_CHAR_SIU")
if not TOKEN:
    raise ValueError("❌ 找不到 DISCORD_TOKEN_CHAR_SIU，請確認環境變數或 .env")

# ======================
# 啟動 keep_alive（會啟一個簡單的網頁伺服器）
# ======================
keep_alive()

# ======================
# Intents 與 Bot 設定
# ======================
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="#", intents=intents)

# ======================
# 關鍵字回覆設定
# ======================
RESPONSES = {
    "hey 叉燒": "我是叉燒🐶，大家做數據加油加油🙌",
    "叉燒晚安": "叉燒也要睡覺了😴大家晚安🐶早點休息喔💤",
    "晚安叉燒": "晚安晚安🐶叉燒要睡了💤",
    "叉燒": "我是叉燒，媽媽最愛我了🥰，歡迎你加入群組，置頂版規記得要去看喔🐶"
}

# ======================
# 事件：上線
# ======================
@bot.event
async def on_ready():
    print(f"✅ 機器人已登入 --> {bot.user} (id={bot.user.id})")

# ======================
# 使用 listen 監聽訊息（不覆蓋 commands）
# ======================
@bot.listen("on_message")
async def remind(message):
    # 忽略來自機器人的訊息（包含自己）
    if message.author.bot:
        return

    # debug：確認有收到訊息
    print(f"[MESSAGE] {message.author} in #{getattr(message.channel, 'name', 'DM')}: {message.content}")

    msg_lower = message.content.lower()
    for key, reply in RESPONSES.items():
        if key in msg_lower:
            await message.channel.send(reply)
            break

# ======================
# 指令：#叉燒、#hello、#ping、#helpme
# ======================
@bot.command(name="叉燒")
async def charsiu_cmd(ctx):
    await ctx.send("我是機器人叉燒🐶")

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention}! 我是玲玲的叉燒 😄")

@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! 🏓 延遲: {round(bot.latency*1000)}ms")

@bot.command()
async def helpme(ctx):
    await ctx.send(
        "指令列表:\n"
        "#叉燒 - 叉燒自我介紹\n"
        "#hello - 打招呼\n"
        "#ping - 測試延遲\n"
    )

# ======================
# 啟動 Bot
# ======================
if __name__ == "__main__":
    bot.run(TOKEN)
