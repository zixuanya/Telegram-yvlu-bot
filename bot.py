import random
import sqlite3
from pyrogram import Client, filters
from pyrogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent

# 初始化 bot
app = Client(
    "lqybot",
    api_id=123456,  # 替换为你的 API ID
    api_hash="22222222222",  # 替换为你的 API Hash
    bot_token="12334567:abcde"  # 替换为你的 Bot Token
)

# 获取随机语录
def get_random_yvlu():
    conn = sqlite3.connect('yvlu.db')
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM yvlu_table")
    count = cursor.fetchone()[0]
    random_index = random.randint(0, count - 1)
    cursor.execute(f"SELECT content FROM yvlu_table LIMIT 1 OFFSET {random_index}")
    result = cursor.fetchone()

    conn.close()

    return result[0] if result else "未找到语录"

# 更改下面的filters.regex(r"^6000元出来爆典$")里的内容达到自己的发送信息设置和filters的相关命令
# 当然，你也可以更改regex的命中键来实现不同的效果
@app.on_message(filters.text & filters.regex(r"^6000元出来爆典$") | filters.command("lqyyvlu"))
async def send_random_yvlu(client, message):
    yvlu = get_random_yvlu()
    await message.reply_text(yvlu)

@app.on_inline_query()
async def inline_query_handler(client, inline_query: InlineQuery):
    yvlu = get_random_yvlu()

    results = [
        InlineQueryResultArticle(
            title="听听某人的小语录🤓", # inline 模式的 tittle
            input_message_content=InputTextMessageContent(yvlu)
        )
    ]
    
    await inline_query.answer(results=results, cache_time=1)

# 启动 bot
app.run()
