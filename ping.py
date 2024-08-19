import requests
import time


def ping(url) -> bool:
    try:
        response = requests.get(url, timeout=1)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False


if __name__ == '__main__':
    url = 'https://alwayson-bcdcg5hwajfcc4av.eastus-01.azurewebsites.net/'
    while True:
        print(f'Pinging {url}...')
        for i in range(3):
            print(time.strftime('%Y-%m-%d %H:%M:%S',
                  time.localtime()), " -> ", end='')
            if ping(url):
                print('Ping successful')
            else:
                print('Ping failed')
        print('Sleeping for 30 minutes...')
        time.sleep(1800)
