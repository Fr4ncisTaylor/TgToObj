<h1 align="center">{ Telegram api To Object }</h1>
<h4 align="center">Parser telegram API BOT updates to object.</h4>

* * *

## Install 

* Pip ```pip install tg-to-obj```

* Git Clone: ```git clone https://github.com/francis-taylor/TgToObj/ && cd TgToObg && python setup.py install```

## Basic use

_I will be using the [Amanobot](https://pypi.org/project/amanobot/) framework to receive [api updates](https://core.telegram.org/bots/api#update)._

```python
import amanobot
import tg_to_obj

bot = amanobot.Bot('1111560977:AAGUffJO2TEw49v81bsPbtWXKR4mYVejvuA')

for i in bot.get_updates():
  print("Input:", tg_to_obj.Make(msgs).update_type) ## get the type of update
```

**the field from has been changed to from_user, as it is a python obj declared by default.**
