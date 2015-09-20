import plugins
import requests
import json

def btc(bot, event):
    s = requests.Session()
    r = s.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    a = r.json()
    output = "The current price of Bitcoin is ${}".format(a['bpi']['USD']['rate'])
    yield from bot.coro_send_message(event.conv, output)

def _initialise(bot):
    plugins.register_user_command(["btc"])
