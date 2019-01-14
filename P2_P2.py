import requests
import os
import urllib.request, json,sys
a=sys.argv[1]
os.chdir('D:/Python/Data_Analysis/venv/History')
link = str('https://fantasy.premierleague.com/drf/element-summary/'+a)

with urllib.request.urlopen(link) as url:
    data = json.loads(url.read().decode())
with open('result_P2.json', 'w') as fp:
    json.dump(data, fp)