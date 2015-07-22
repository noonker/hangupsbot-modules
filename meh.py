import re, shlex

import hangups

from hangupsbot.utils import text_to_segments
from hangupsbot.handlers import handler, StopEventHandling
from hangupsbot.commands import command
import requests
from bs4 import BeautifulSoup

@handler.register(priority=5, event=hangups.ChatMessageEvent)
def handle_command(bot, event):
    """Handle command messages"""
    if not event.text:
        return
    if ".meh" in  event.text:
        s = requests.Session()
        r = s.get("http://meh.com")
        soup = BeautifulSoup(r.content)
        sout = soup.h2
        for meh_string in sout.stripped_strings:
            (repr(meh_string))
        yield from event.conv.send_message(text_to_segments("Meh " + meh_string + " https://meh.com"))

