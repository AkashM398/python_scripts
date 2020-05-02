import requests
from bs4 import BeautifulSoup

startUrl = input("Enter the URl")
response = requests.get(startUrl)
html = response.text

soup = BeautifulSoup(html, 'lxml')
photoUrl = soup.find("meta", property="og:image")['content']
print(photoUrl)

photoName = photoUrl[-25:-6]
print('Name is:' + photoName)

requestUrl = requests.get(photoUrl)
f = open(photoName + '.jpg', 'ab')
f.write(requestUrl.content)
print('processing...')
f.close()
print('Download complete')