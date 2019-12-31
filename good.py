# (c) @UniBorg

from telethon import events
import asyncio
from collections import deque


@borg.on(events.NewMessage(pattern=r"\.moon animation", outgoing=True))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list('🌗🌘🌑🌒🌓🌔🌕🌖'))
for _ in range(32):
    await asyncio.sleep(0.1)
    await client.edit_message(event.to_id, message=event.id, text=''.join(deq))
    deq.rotate(1)
for i in ('G🌗🌘🌑🌒🌓🌔🌕🌖 ㅤ',
          'Go🌘🌑🌒🌓🌔🌕🌖ㅤㅤ',
          'Goo🌑🌒🌓🌔🌕🌖ㅤㅤ',
          'Good🌒🌓🌔🌕🌖ㅤㅤㅤ',
          'Good 🌓🌔🌕🌖ㅤㅤㅤ',
          'Good N🌔🌕🌖ㅤㅤㅤㅤ',
          'Good Ni🌕🌖ㅤㅤㅤㅤ',
          'Good Nig🌖ㅤㅤㅤㅤㅤ',
          'Good Nighㅤㅤㅤㅤㅤ',
          'Good Nightㅤㅤㅤㅤㅤ',
          'Good Night!ㅤㅤㅤ🦉'):
    await asyncio.sleep(0.1)

    await client.edit_message(event.to_id, message=event.id, text='<i>{}</i>'.format(i), parse_mode='html')