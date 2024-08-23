f = '''http://cPanelLogin.link:port|username|password'''

lines = f.split('\n')
import requests
h = 0
for line in lines:
    if line.startswith('http'):
        url = line.split('|')[0]
        user = line.split('|')[1]
        passw = line.split('|')[2]
        try:
            r = requests.get(url)
            print(r.status_code,f': {url} | {user} | {passw}')
        except:
            print('error')
        h += 1
