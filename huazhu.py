import os
import requests
import pytz
import json
from datetime import datetime
from os import environ



url = "https://hweb-mbf.huazhu.com/api/signIn"

headers = {
    "Host": "hweb-mbf.huazhu.com",
    "Connection": "keep-alive",
    "Accept": "application/json, text/plain, */*",
    "Sec-Fetch-Site": "same-site",
    "Accept-Language": "zh-CN,zh-Hans;q=0.9",
    "Accept-Encoding": "gzip, deflate, brgzip, deflate, br",
    "Sec-Fetch-Mode": "cors",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "https://campaign.huazhu.com",
    "User-Agent": "HUAZHU/ios/iPhone14,3/16.3.1/9.9.0/HUAZHU/ios/iPhone14,3/16.3.1/9.9.0/Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
    "Client-Platform": "APP-IOS",
    "Referer": "https://campaign.huazhu.com/",
    "User-Token": "null",
    "Content-Length": "14",
    "Sec-Fetch-Dest": "empty",
    "Cookie": environ.get("huazhu_cookie")
}
beijing_tz = pytz.timezone('Asia/Shanghai')
beijing_time = datetime.now(beijing_tz)
data = f"state=1&day={beijing_time.day}"

response = requests.post(url, headers=headers, data=data)