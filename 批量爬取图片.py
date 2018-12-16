import requests
import os
from bs4 import BeautifulSoup


i = 0
url = "http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%B5%E7%C4%D4%B8%DF%C7%E5%B1%DA%D6%BD&fr=ala&ala=1&alatpl=adress&pos=0&hs=2&xthttps=000000"
'''
html = requests.get(url)
html.encoding = html.apparent_encoding
soup = BeautifulSoup(html.text, "html.parser")
for url in soup.find("img"):
    root = "F://image//"
    path = root +url("src").split('/')[-1]
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        i = i + 1
        r = requests.get(url("src"))
        with open(path, 'wb') as f:
            f.write(r.content)
            print("保存成功第%d幅图片" %i)
    else:
        print("文件已存在")

'''
