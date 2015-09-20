import plugins
import re

import requests
from bs4 import BeautifulSoup
def _scan_for_triggers(bot, event, *args):
    urlgex = re.compile(
    r'(\Apraise be)', re.IGNORECASE)
    if urlgex.match(event.text):
        output = "Praise be"
        yield from bot.coro_send_message(event.conv, output)

def _initialise(bot):
    plugins.register_handler(_scan_for_triggers)
