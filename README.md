# Telegram 语录 Bot

这个 Bot 的原先模型为 [lqy6000bot] 所使用

回复 *** 字段或者命令即可发送相关语录信息（需要对源代码进行修改）

兼容inline模式，自行配置后使用

使用makedb创造语录文件sqllite db 便于管理和使用

### 使用方法

clone该项目，放在自己喜欢的地方，创建 venv 环境（特别建议）

```
git clone https://github.com/zelrgezhi/Telegram-yvlu-bot.git
```

```
# 创建 venv
python3 -m venv venv
```

```
# 开启 venv
source venv/bin/activate
```

使用 pip3 下载需要的组件

```
pip3 install -r requirements.txt
```

更改 Bot.py 和 Makedb.py 调整至自己的配置，随后运行makedb.py创建db数据库

一切准备完成后，便可启动bot了，保活可以通过systemd 和 screen 的方式保活，文档提供systemd，便不再讲解

