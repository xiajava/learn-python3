#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import base64


def safe_base64_decode(s):
    mod = int(len(s)) % 4
    if mod != 0:
        s += b'=' * (4 - mod)
    return base64.urlsafe_b64decode(s)


# 测试:
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('Pass')
