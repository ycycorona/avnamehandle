import requests
proxy_addr = '127.0.0.1:10099'
url = 'http://www.javlibrary.com/cn/star_list.php?prefix=E&page=1'
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
    'Host': 'www.javlibrary.com',
    'Referer': 'http://www.javlibrary.com/cn/?v=javli7joye',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7,zh-TW;q=0.6',
    'DNT': '1',
    'Upgrade-Insecure-Requests': '1',
    'Connection': 'keep-alive',
    'Cookie': '__cfduid=d716b3c04427e0683e6975c979031f28c1532748927; timezone=-480; __atuvc=1%7C34; userid=ycy421; session=YLRT5sCbxkCe2s14%2BIxwX8UjCGuN21af0kFW%2BLfD%2FI2YVZQHzFMp9WRUbjN4A6kgMbcceJzzPTavvM%2FuY8JUgw%3D%3D+%3B+3baae08b468bac91d30575e551efdc8977e4c8ae+%3B+-32768; cf_clearance=7869683c1517dd028502aea82723c9c3690e820b-1539881699-3600-150'
}
proxy = {
    'http': 'http://' + proxy_addr,
    'https': 'https://' + proxy_addr
}

res = requests.get(url, proxies=proxy, headers=headers)

print(res.text)