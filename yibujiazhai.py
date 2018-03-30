#异步加载


import requests
import re
from bs4 import BeautifulSoup

headers = {
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}
urls = ['https://www.pexels.com/?page={}'.format(str(i)) for i in range(1,2)]#异步加载时的url
photos = []#存放下载的url
for url in urls:
    web_data = requests.get(url,headers = headers)
    soup = BeautifulSoup(web_data.text,'lxml')
    imgs = soup.select('body > div > div.photos > article > a > img')
    for img in imgs:
        photo = img.get('src')#get 获取img标签的src
        photos.append(photo)
    path = 'G://yibu/'

    for item in photos:
        data = requests.get(item,headers = headers)#根据src获取图片地址
        photo_name = re.findall('\d+/(.*?)\?au',item)
        print(photo_name)
        if photo_name:

            fp = open(path + photo_name[0], 'wb')
            fp.write(data.content)
            fp.close()