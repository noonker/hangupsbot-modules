import re

import hangups

from hangupsbot.utils import text_to_segments
from hangupsbot.handlers import handler, StopEventHandling
from hangupsbot.commands import command
import requests
from bs4 import BeautifulSoup

@handler.register(priority=5, event=hangups.ChatMessageEvent)
def handle_command(bot, event):
    if not event.text:
        return
    urlgex = re.compile(
    r'^(?:http|ftp)s?://' # http:// or https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # domain...
    r'localhost|' # localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|' # ...or ipv4
    r'\[?[A-F0-9]*:[A-F0-9:]+\]?)' # ...or ipv6
    r'(?::\d+)?' # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    for item in event.text.split(" "):
        if urlgex.match(item):
            s = requests.Session()
            r = s.get(item)
            soup = BeautifulSoup(r.content)
            yield from event.conv.send_message(text_to_segments(soup.title.string))

