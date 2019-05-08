# coding:utf-8
__author__ = 'xxj'

import sys
import time
import math
import os
from rediscluster import StrictRedisCluster
import json
import re
import Queue
import lxml.etree
import requests
import re
import datetime
import threading
from threading import Lock
from Queue import Empty
from requests.exceptions import ReadTimeout, ConnectionError, ConnectTimeout

reload(sys)
sys.setdefaultencoding('utf-8')
headers = {
    # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    # 'Accept-Language': 'zh-CN,zh;q=0.9',
    # 'Cache-Control': 'no-cache',
    # 'Connection': 'keep-alive',
    # 'Content-Length': '91',
    # 'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': '_ga=GA1.2.1721220333.1554968377; _gid=GA1.2.1773673400.1557128627; Hm_lvt_6262479c0cdc4169b77920e25151a60f=1554969305,1557128627; Hm_cv_6262479c0cdc4169b77920e25151a60f=1*email*guest!*!*!1*role*guest; _gat_gtag_UA_8981755_3=1; XSRF-TOKEN=eyJpdiI6ImtLazhjMjl0eTBoaGs5TmM0NEcySHc9PSIsInZhbHVlIjoic2Vkang5WHQ1b0FERUZvaXVXTGlYNjBXeU1EN0xqRTR2U2luNExRdGdhdGVjWU1PVEJZZGR0c2FybmVOQ3luMExnK2YxcGh1MkwxeTE3SVNjU3RIXC9RPT0iLCJtYWMiOiJiMzkyODUwYTdiNTdmMDgyODJkMmI5NzhmMjViODI4NTlmNTk3YjIyY2U0ZDhkNTFjYjMyZTIyY2M1YjU3MTkwIn0%3D; toobigdata_session=eyJpdiI6IlwvbkRwcmdjUmp1TzRRWlJ5b3RibVhRPT0iLCJ2YWx1ZSI6IlZWZ3NodUxYOWtUTXZBQ1RoVVNOd3dhRlwvc3Y3Qk5jSGdHbkFGcTBydjhTZnRGeHdzcyt0Q3RrdW12dFZ0T2ZoNG5oQlRjZEpaakd6QlFVN0xmejczdz09IiwibWFjIjoiNGVhMjk2ZjRmOTYzMjY4YTE1MzQxNGZiOWM1YmE1MjczNzkxOTkzYzk2N2M1Njg5NGQzNjZlZmU3YmRkMTZjMCJ9; Hm_lpvt_6262479c0cdc4169b77920e25151a60f=1557193594',
    # 'Host': 'kolranking.com',
    # 'Cookie': '_ga=GA1.2.1721220333.1554968377; _gid=GA1.2.1773673400.1557128627; Hm_lvt_6262479c0cdc4169b77920e25151a60f=1554969305,1557128627; _gat_gtag_UA_8981755_3=1; Hm_cv_6262479c0cdc4169b77920e25151a60f=1*email*guest!*!*!1*role*guest; XSRF-TOKEN=eyJpdiI6IlpDTU53VWYxWkFlMmRMUVlNMUN5d0E9PSIsInZhbHVlIjoiYk1UN2FxcFVwdTR6TWduTFhGQTErczBvV2JCY2I1NWlHOVlFTW5VVjZsVWVDRU54WjgxdVlDMzJVZ2JMcm1Zd09zVlJPeEY4emM0SEt3a2RYXC9DVU9RPT0iLCJtYWMiOiJlOWE3YTUxODM3NTljNmI0MjY5MjVkM2QzN2NlY2JmMGJkOTcyMzQ0YmQ3NzI1MGU0NTg4MjE4ZjBkNWZlZTI2In0%3D; toobigdata_session=eyJpdiI6IjNDWGxHRDNPZ0pcL3dtUkJKSDh0dFNRPT0iLCJ2YWx1ZSI6Ijh3aGg3bjY0SHBDRGZSXC93Wndrb0RROWYwemJnUVR0RTE2amlnRGVNMlVnbWQ2QlI5eFNkelFOVk5jTkJlXC9cL3FOWmZHUUlJOXlkaVlaQkxMcmJTdndnPT0iLCJtYWMiOiIwNDUwOGYyYTE1MzkyYmM3NjcxZTlkZDhjNGI1YmZiNzRhMzUwYWRjMjc5NTA4ODY2ZWU2YmIwNjllYWRkZGYzIn0%3D; Hm_lpvt_6262479c0cdc4169b77920e25151a60f=1557198676',
    # 'Origin': 'https://kolranking.com',
    # 'Pragma': 'no-cache',
    # 'Referer': 'https://kolranking.com/login',
    # 'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
}


def douyin_kol_login():
    data = {
        # '_token': 'n0PicQcKeOUTS4u6DZxrSCslXXttLluHokpPqedj',
        # _token: RUEWSNpNkKFLvl8FJoRamonb8HDCrmnQF1Bq3cMj
        # '_token': 'KIo1VzaDfTEUM76opGgg8YVsNbOaRSRKK6Lw8ctP',
        'email': 'dhfhjhfeu@163.com',
        'password': 'www12345',
    }
    url = 'https://kolranking.com/login'
    response = requests.post(url=url, headers=headers, data=data, timeout=10)
    print response.status_code
    print response.headers
    print response.headers.get('Set-Cookie')
    print response.text


def douyin_kol_selenium_login():
    pass


def douyin_kol_detail_parse():
    headers = {
        # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        # 'Accept-Encoding': 'gzip, deflate, br',
        # 'Accept-Language': 'zh-CN,zh;q=0.9',
        # 'Cache-Control': 'no-cache',
        # 'Connection': 'keep-alive',
        # 'Cookie': '_ga=GA1.2.1721220333.1554968377; _gid=GA1.2.1773673400.1557128627; Hm_lvt_6262479c0cdc4169b77920e25151a60f=1554969305,1557128627; Hm_lpvt_6262479c0cdc4169b77920e25151a60f=1557196031; Hm_cv_6262479c0cdc4169b77920e25151a60f=1*email*dhfhjhfeu%40163.com!*!*!1*role*free; XSRF-TOKEN=eyJpdiI6InE0aVI2TlFyUWNFSEFCczJ2bWhkM3c9PSIsInZhbHVlIjoiYTBGRzJacVcxZ2E2aDkzRWhVXC83c0NLaXFHaG5XdjR6S2NUaGNQOEF5K0p0U0J1Nk5Sc2w4ZVMxVldPajc3QnpDSXV1eGp5KzkwdmZiaXpKaGpzZzBRPT0iLCJtYWMiOiIyNDdlYmVlYzljYjE5YzVlNDY3MDc1ZDIxYmE5NmU1OGQxYzE4MzdiNDUzZjIzNWFmMjQyODVjZDJhNTdhY2VhIn0%3D; toobigdata_session=eyJpdiI6ImlmQ0k2REkrQk1RUzZGWmxRc21ud2c9PSIsInZhbHVlIjoiQ2VBVlFZMmozcUw5WXA3YXQ4dlRDek1tekFRR2dEVVNXVThzeEM5bjBMNnZ3SkRCcEU5ZTFMT2F6dE1yVFNDQVJ1YXlBMVduQTJsM3ZKM25FUGwyVlE9PSIsIm1hYyI6IjEwNTY4MmI0MThiYjRkMTNiNmFiYWRiMDliNzc5MzgyZWQ3NDZjNzlhZGZjOTM4NjkwNTJjZWU3ZjA4ZDk3NzkifQ%3D%3D',
        # 'Cookie': 'XSRF-TOKEN=eyJpdiI6InE0aVI2TlFyUWNFSEFCczJ2bWhkM3c9PSIsInZhbHVlIjoiYTBGRzJacVcxZ2E2aDkzRWhVXC83c0NLaXFHaG5XdjR6S2NUaGNQOEF5K0p0U0J1Nk5Sc2w4ZVMxVldPajc3QnpDSXV1eGp5KzkwdmZiaXpKaGpzZzBRPT0iLCJtYWMiOiIyNDdlYmVlYzljYjE5YzVlNDY3MDc1ZDIxYmE5NmU1OGQxYzE4MzdiNDUzZjIzNWFmMjQyODVjZDJhNTdhY2VhIn0%3D',
        # 'Cookie': 'toobigdata_session=eyJpdiI6ImlmQ0k2REkrQk1RUzZGWmxRc21ud2c9PSIsInZhbHVlIjoiQ2VBVlFZMmozcUw5WXA3YXQ4dlRDek1tekFRR2dEVVNXVThzeEM5bjBMNnZ3SkRCcEU5ZTFMT2F6dE1yVFNDQVJ1YXlBMVduQTJsM3ZKM25FUGwyVlE9PSIsIm1hYyI6IjEwNTY4MmI0MThiYjRkMTNiNmFiYWRiMDliNzc5MzgyZWQ3NDZjNzlhZGZjOTM4NjkwNTJjZWU3ZjA4ZDk3NzkifQ%3D%3D',
        'Cookie': 'toobigdata_session=eyJpdiI6InRlM0pCa24wV3BKNW0zd0lGendwT2c9PSIsInZhbHVlIjoid0NhdFpCVStCbUFCNlQzclNCYzFsOFhxMlpadFA2UXN6TWdQWDVJUU9nY1FUNmZQOFpwNUIwNEo5OVNLSXZ4eDBJWWlFejJYcTZiYjl3eDd6OUV5bFE9PSIsIm1hYyI6IjBhNGM3MWIwY2Y3NDcyODIxNzY2NDNkNjBiZDAyM2E3YTRjZjZjOGRjODgyNDcxMzA4NjAwNWE0M2NhNDkwNjYifQ%3D%3D;',
        # 'Host': 'kolranking.com',
        # 'Pragma': 'no-cache',
        # 'Referer': 'https://kolranking.com/?ot=DESC&order=follower_count&page=3',
        # 'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
    }
    url = 'https://kolranking.com/douyin/user/20577'
    response = requests.get(url=url, headers=headers, timeout=10)
    print response.status_code
    print response.text


def douyin_kol():
    url = 'http://ip.cn'
    print time.strftime('[%Y-%m-%d %H:%M:%s]'), '抖音url：', url


def main():
    # douyin_kol_login()    # 对于登录而言，主要是为了获取到登录后的toobigdata_session参数
    douyin_kol_detail_parse()
    # douyin_kol()


if __name__ == '__main__':
    main()