#!/usr/bin/env python3

import requests
import sys
import contextlib
from requests.auth import HTTPBasicAuth

def requestdehashed():
    email = []
    passwd = []
    if len(sys.argv) > 1:
        host = sys.argv[1]
        print("------------------ PUT TLD with the domain plz ------------------")
    else:
        print("Usage : ./dehashedReq.py domain.tld")
        quit()
    url = 'https://api.dehashed.com/search?query=email:' + host+"&size=3000"
    headers = {"Accept": "application/json"}
    r = requests.get(url, auth=HTTPBasicAuth('<email>', '<apikey>'),
                     headers=headers)
    if r.status_code == 200:
        loaded_results = r.json()
        try:
            path_mail = host + '_mail.txt'
            path_passwd = host + '_passwd.txt'
            for i in loaded_results["entries"]:
                value = True
                email.append((i["email"]))
                if email.count((i["email"])) > 1:
                    email.remove((i["email"]))
                    value = False
                if value == True:
                    password = (i["password"])
                    if len(password) <= 1:
                        passwd.append((i["hashed_password"]))
                        # if passwd.count((i["hashed_password"])) > 1:
                        #     passwd.remove((i["hashed_password"]))
                    else:
                        passwd.append((i["password"]))
                    value = True
            print("Balance left: " + str(loaded_results["balance"]))
            print("End of request, file has been created , the path : ", path_mail)
        except TypeError:
            print("No result found in database")
    else:
        print("API key missing")
    with open(path_mail, 'w+') as f:
        with contextlib.redirect_stdout(f):
            for i in email:
                print(i)
    with open(path_passwd, 'w+') as f:
        with contextlib.redirect_stdout(f):
            for i in passwd:
                print(i)

if __name__ == '__main__':
    requestdehashed()
