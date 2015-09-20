import plugins
import requests
from bs4 import BeautifulSoup

def meh(bot, event):
    s = requests.Session()
    r = s.get("http://meh.com")
    soup = BeautifulSoup(r.content)
    sout = soup.h2
    for meh_string in sout.stripped_strings:
        (repr(meh_string))
        output = "Meh {} https://meh.com".format(meh_string)
    yield from bot.coro_send_message(event.conv, output)

def _initialise(bot):
    plugins.register_user_command(["meh"])
