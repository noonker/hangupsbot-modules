import re, shlex
import json
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
    if ".game" in event.text:
        print(event.text)
        print(event.text.split(" "))      
        output = event.text.split(".game ")[1]
        s = requests.Session()
        r = s.get('https://api.twitch.tv/kraken/streams', params={'game':output})
        a = json.loads(r.text)
        if a["_total"] == 0:
            yield from event.conv.send_message(text_to_segments("Please check your input"))
            return
        else:
            yield from event.conv.send_message(text_to_segments("The top streamer for {} is {}.\n {}".format(output, a["streams"][0]["channel"]["display_name"], a["streams"][0]["channel"]["url"])))

