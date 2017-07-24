#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib, re, json


def get_md5(password):
    m = hashlib.md5()
    m.update(password.encode('utf-8'))
    return m.hexdigest()


def register(user, password):
    try:
        with open(r'D:\test.txt', 'r') as f:
            db = json.load(f)
    except:
        db = {}
    dbr = db
    if user in dbr:
        print('username exist,cant register.')
        return False
    if not re.match('\w+', user):
        print('username is invalid.')
        return False
    if not re.match('\w+', password):
        print('password is invalid.')
        return False
    dbr[user] = get_md5(password + user + 'the-Salt')
    with open(r'D:\test.txt', 'w') as f:
        json.dump(dbr, f)
    print('register success.')
    return True


def login(user, password):
    try:
        with open(r'D:\test.txt', 'r') as f:
            dbl = json.load(f)
    except:
        print('Dict does not exist.')
        return False
    if user not in dbl:
        print('User does not exist.')
        return False
    if get_md5(password + user + 'the-Salt') == dbl[user]:
        print('login success.')
        return True
    else:
        print('Password incorrect.')
        return False


user_r = input('register user:')
pw_r = input('register password:')
register(user_r, pw_r)

user_l = input('login user:')
pw_l = input('login password:')
print(login(user_l, pw_l))
