import plugins
import requests

def twitch(bot, event, *args):
    term = " ".join(args)
    s = requests.session()
    r = s.get('https://api.twitch.tv/kraken/streams', params={'game':term})
    a = r.json()
    if a["_total"] == 0:
        output = "Please check your input"
    else:
        output = "The top streamer for {} is {}.\n {}".format(term, a["streams"][0]["channel"]["display_name"], a["streams"][0]["channel"]["url"])
    yield from bot.coro_send_message(event.conv, output)

def _initialise(bot):
    plugins.register_user_command(["twitch"])
