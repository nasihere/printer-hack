
import requests

import subprocess

def winWhoAmI():
    return subprocess.run(['whoami', '-upn'], stdout=subprocess.PIPE, encoding='utf-8').stdout

def macWhoAmI():
    return subprocess.run(['whoami'], stdout=subprocess.PIPE, encoding='utf-8').stdout

def registerUserName(username, WS_CONNECTION_ID):
    print("regiset User Name")
    url = 'http://ec2-3-132-213-115.us-east-2.compute.amazonaws.com:3002/register/?socket=enable&username='+username.strip()+"&connectionId="+WS_CONNECTION_ID
    #myobj = {'username': username.strip(), "connectionId": WS_CONNECTION_ID}
    #print(myobj)
    x = requests.get(url)
    #print(x.text)