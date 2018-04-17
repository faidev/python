#!/usr/bin/env python3
import getpass

_username = "wayne"
_password = "123456"
username = input("username:")
password = getpass.getpass("password:")

print(username, password)

if _username == username and _password == password:
    print("welcome user {name} login...".format(name=username))
else:
    print("invalid username or password!")
