#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#シーザー暗号 サンプル01の入力版
import cgitb

# 平文
PLAIN = input()

# 秘密鍵
KEY = 3

# 以下に、記述してください。
enc = ""

for char in list(PLAIN):
    ASCII = ord(char)
    num = ASCII - 97
    num = (num + KEY) % 26
    ASCII = num + 97
    enc += chr(ASCII)

print(enc)