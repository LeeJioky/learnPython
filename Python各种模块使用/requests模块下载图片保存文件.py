import requests

url = 'https://support.apple.com/library/content/dam/edam/applecare/images/en_US/applecare/ergo-head-neck.png'
r = requests.get(url)
with open('chun.jpg', 'wb') as fo:
    fo.write(r.content)
