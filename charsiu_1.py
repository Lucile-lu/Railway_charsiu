import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# ======================
# 讀取環境變數
# ======================
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN_CHAR_SIU")
if not TOKEN:
    raise ValueError("❌ 找不到 DISCORD_TOKEN_CHAR_SIU，請確認 .env 或環境變數")

# ======================
# Bot 設定
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

WELCOME_CHANNEL_NAME = "歡迎訊息與相關規則🎉"

# ======================
# Bot 上線事件
# ======================
@bot.event
async def on_ready():
    print(f"✅ 機器人已登入 --> {bot.user} (id={getattr(bot.user, 'id', 'Unknown')})")

# ======================
# 新成員加入事件
# ======================
@bot.event
async def on_member_join(member):
    if member.bot:
        return
    channel = discord.utils.get(member.guild.text_channels, name=WELCOME_CHANNEL_NAME)
    if channel:
        await channel.send(
            f"👋 我是機器人叉燒🐶\n"
            f"✨ 歡迎 {member.mention} 加入鄺玲玲的天使金毛🦮🪽\n"
            f"📌 請先閱讀群規（置頂/公告），一起營造乾淨追星環境🤍"
        )

# ======================
# 訊息監聽（關鍵字回覆）
# ======================
@bot.listen("on_message")
async def remind(message):
    if message.author.bot:
        return
    msg_lower = message.content.lower()
    for key, reply in RESPONSES.items():
        if key in msg_lower:
            if message.channel:
                await message.channel.send(reply)
            break

# ======================
# 指令
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
# 自動重連與啟動
# ======================
def run_bot():
    while True:
        try:
            bot.run(TOKEN)
        except Exception as e:
            print(f"⚠️ Bot 崩潰或斷線，正在重啟... 錯誤: {e}")

if __name__ == "__main__":
    run_bot()
