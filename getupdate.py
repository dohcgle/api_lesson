#  @tutorial_ulugbek_bot

import requests
from pprint import pprint
token = '1610753174:AAHpqhQf1kdJ1AFOKdZFS14gleR76XwzSHQ'
url = f'https://api.telegram.org/bot{token}/getUpdates'
r = requests.get(url)
data = r.json()
updates = data['result']
pprint(updates)