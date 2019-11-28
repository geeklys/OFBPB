
from datetime import datetime

import nonebot
import pytz
from aiocqhttp.exceptions import Error as CQHttpError

he = 36
aoye = 0
cusi = 0

grp = 336572166
test_grp = 114366579

def notice():
    global he, aoye, cusi
    hour = datetime.now().hour
    if hour >=6 and hour <= 22:
        msg = f'喝水提醒 +{he}'
        he += 1
    elif hour == 23 or (hour >= 0 and hour <= 1):
        msg = f'熬夜提醒 +{aoye}  ━┳━　━┳━'
        aoye += 1
    else:
        msg = f'猝死提醒 +{cusi} 记得保存工作/游戏'
        cusi += 1
    return msg
    



@nonebot.scheduler.scheduled_job('cron', hour='*')
async def _():
    bot = nonebot.get_bot()
    msg = notice()
    await bot.send_group_msg(group_id=grp, message=msg)
