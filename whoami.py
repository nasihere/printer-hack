
import requests

import subprocess

def winWhoAmI():
    return subprocess.run(['whoami', '-upn'], stdout=subprocess.PIPE, encoding='utf-8').stdout

def macWhoAmI():
    return subprocess.run(['whoami'], stdout=subprocess.PIPE, encoding='utf-8').stdout

def registerUserName(username, WS_CONNECTION_ID):
    print("regiset User Name")
    url = 'http://localhost:3000/register'
    myobj = {'username': username.strip(), "connectionId": WS_CONNECTION_ID}
    print(myobj)
    x = requests.post(url, data = myobj)
    print(x.text)