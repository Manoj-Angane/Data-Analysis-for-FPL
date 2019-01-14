import requests
import os
import urllib.request, json

os.chdir('D:/Python/Data_Analysis/venv')
link = 'https://fantasy.premierleague.com/drf/bootstrap-static'

with urllib.request.urlopen(link) as url:
    data = json.loads(url.read().decode())
with open('result.json', 'w') as fp:
    json.dump(data, fp)