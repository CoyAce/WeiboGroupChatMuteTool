import requests
import sys
import json


def send(code='4'):
    session = requests.session()
    config = json.load(open('config.json'))
    headers = {
        'Host': 'api.weibo.com',
        'User-Agent': 'PostmanRuntime/7.28.2',
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://api.weibo.com/chat/',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '265',
        'Connection': 'keep-alive',
        'Cookie': config['cookie']
    }

    data = {
        # 1开启，4关闭
        'speech_forbid': code,
        'id': config['id'],
        'source': config['source'],
    }

    url = 'https://api.weibo.com/webim/groupchat/update.json'
    r = session.post(url, data=data, headers=headers)
    print(r.content.decode('utf-8'))

if __name__ == '__main__':
    send(sys.argv[1])