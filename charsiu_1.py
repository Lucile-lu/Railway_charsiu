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
# 回覆設定（文字/圖片/GIF）
# ======================
# 統一管理，方便後續新增
RESPONSES_DATA = {
    "hey 叉燒": {"text": "我是叉燒🐶，大家做數據加油加油🙌"},
    "叉燒晚安": {"text": "叉燒也要睡覺了😴大家晚安🐶早點休息喔💤",
                "file": "night1.gif"},
    "晚安叉燒": {"text": "晚安晚安🐶叉燒要睡了💤",
                 "file": "night2.gif"},
    "叉燒": {"text": "我是叉燒，媽媽最愛我了🥰，歡迎你加入群組，置頂版規記得要去看喔🐶",
            "file": "play with charsiu.gif"},  
    "驕傲": {"file": "proud.gif"},
    "臭": {"file": "smelly.gif"},
    "喔～": {"file": "oh.gif"},
    "蛤": {"file": "hhu.gif"},
    "開心": {"file": "happy.gif"},
    "不喜歡": {"file": "unhappy.gif"},
    "好吃": {"file": "yummy.gif"},
    "生氣": {"file": "angry.gif"},
    "謝謝大家": {"file": "thx.gif"},
    "看了什麼": {"file": "wtf.gif"},
    "嗯？": {"file": "umm.gif"},
    "很棒": {"file": "good.jpg"},
    "氣死": {"file": "hun.gif"},
    "哇": {"file": "wow.gif"},
    "厲害": {"file": "see.gif"},
    "這是什麼": {"file": "what.jpg"},
    "滾": {"file": "roll.gif"},
    "累了": {"file": "headache.gif"},
    "認真嗎": {"file": "seriously.gif"},
    "不行": {"file": "no.gif"},
    "早安": {"file": "morning1.gif"},
    "聰明": {"file": "smart.gif"},
    "不知道": {"file": "unkwonw.gif"},
    "不信": {"file": "Don't believe it.gif"},
    "好冷": {"file": "cold.gif"},
    "吃飯": {"file": "eat.gif"},
    "愛你": {"file": "luv.gif"},
    "玲嗎": {"file": "me.gif"},
    "都給你": {"file": "all for you.gif"},
    "玲玲啊": {"file": "appear"},
    "再見": {"file": "byebye.gif"},
    "閉眼": {"file": "close eyes.gif"},
    "無聊": {"file": "chew.gif"},
    "不理解": {"file": "well.gif"},
    "辛苦": {"file": "claps.gif"},
    "給我吃": {"file": "eateateat.gif"},
    "不懂": {"file": "scratch.gif"},
    "尷尬": {"file": "awkward.gif"},
    "拒絕": {"file": "nonono.gif"},
    "醒": {"file": "wake.gif"},
    "優秀": {"file": "crown.gif"},
    "走開": {"file": "go away.gif"},
    "算了": {"file": "peace.gif"},



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
# 新成員加入事件
# ======================
@bot.event
async def on_member_join(member):
    if member.bot:
        return
    channel = discord.utils.get(member.guild.text_channels, name=WELCOME_CHANNEL_NAME)
    if channel:
        # 可以同時支援文字 + GIF
        welcome_text = f"👋 我是機器人叉燒🐶\n✨ 歡迎 {member.mention} 加入鄺玲玲的天使金毛🦮🪽\n📌 請先閱讀群規（置頂/公告），一起營造乾淨追星環境🤍"
        gif_path = "chashiu.gif"
        if os.path.exists(gif_path):
            await channel.send(content=welcome_text, file=discord.File(gif_path))
        else:
            await channel.send(welcome_text)

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
