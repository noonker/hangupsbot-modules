import plugins
import re

import requests
from bs4 import BeautifulSoup
def _scan_for_triggers(bot, event, *args):
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
            headers = {'Connection': 'keep-alive', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36'} 
            r = requests.get(item, headers=headers)
            soup = BeautifulSoup(r.content)
            yield from bot.coro_send_message(event.conv, soup.title.string)

def _initialise(bot):
    plugins.register_handler(_scan_for_triggers)
