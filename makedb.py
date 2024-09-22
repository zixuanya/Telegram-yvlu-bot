import sqlite3

conn = sqlite3.connect('yvlu.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS yvlu_table (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content TEXT NOT NULL
)
''')

# 更改下列数据
example_data = [
    "下列均为例子数据，将其替换或者增加条目",
    "以为自己是mygo",
    "七个人凑不出一个妈",
    "这几个人个个出生你有意见吗",
    "你们喝的里面全是敬业",
    "复活赛打不赢了，我会取代你，继承你的医治😭😭😭"
]

def insert_data():
    cursor.executemany("INSERT INTO yvlu_table (content) VALUES (?)", [(data,) for data in example_data])

    # 提交更改
    conn.commit()

insert_data()

cursor.execute("SELECT COUNT(*) FROM yvlu_table")
count = cursor.fetchone()[0]
print(f"已插入 {count} 条数据到 yvlu_table 表中了哦~可以直接调用 Bot.py 啦")

# 关闭连接
conn.close()
