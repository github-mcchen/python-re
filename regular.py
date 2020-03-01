#!/usr/bin/python
# coding: UTF-8

import requests
import re

link = "https://blog.csdn.net/muchong123"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

r = requests.get(link, headers=headers)

pattern_info = re.compile(
    r".*原创.*\"count\">(.*?)<.*粉丝.*\"fan\">(.*?)<.*获赞.*\"count\">(.*?)<.*评论.*\"count\">(.*?)<.*访问.*\"count\">(.*?)<.*",
    re.S)

pattern_standing = re.compile(
    r".*等级:.*title=\"(.*?),.*周排名:.*?_blank\">.*?(\S+).*?</a>.*?积分:.*?>.*?(\d+).*?</dd>.*总排名:.*?target=\"_blank\">.*?(\S+).*?</a>.*",
    re.S)

csdn_info = pattern_info.findall(r.text)
standing_list = pattern_standing.findall(r.text)

for item in csdn_info:
    print("基本信息：\n原创：%s\n粉丝：%s\n获赞：%s\n评论：%s\n访问：%s\n" % (item[0], item[1], item[2], item[3], item[4]))

for item in standing_list:
    print("排名等级：\n等级：%s\n周排名：%s\n积分：%s\n总排名：%s" % (item[0], item[1], item[2], item[3]))
