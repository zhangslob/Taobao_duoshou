#!/usr/bin/env python
# -*- coding: utf-8 -*-

#!/usr/bin/env python
# -*- coding:utf-8 -*-


import requests

url = "https://space.bilibili.com/ajax/member/GetInfo"

payload = {'mid':'42000000','csrf':'null'}

headers = {

    'origin': "https://space.bilibili.com",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "zh-CN,zh;q=0.9,en;q=0.8",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
    'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
    'accept': "*/*",
    'referer': "https://space.bilibili.com/99598680?from=search&seid=18176172860872021389",
    'x-requested-with': "XMLHttpRequest",
    'connection': "keep-alive",
    'cache-control': "no-cache",
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.json())
