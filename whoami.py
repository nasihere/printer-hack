

import subprocess

def winWhoAmI():
    return subprocess.run(['whoami', '-upn'], stdout=subprocess.PIPE, encoding='utf-8').stdout

def macWhoAmI():
    return ubprocess.run(['whoami'], stdout=subprocess.PIPE, encoding='utf-8').stdout
