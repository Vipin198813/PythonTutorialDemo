import img
import requests
import lxml
import img
import bs4

result = requests.get('https://www.example.com/')
print(type(result))
soup = bs4.BeautifulSoup(result.text,'lxml')
print(soup.select('p'))
title = soup.select('title')[0].getText()
print(title)
site_paragraph = soup.select('p')
print(site_paragraph[0])
print(type(site_paragraph))
print(site_paragraph[0].getText())

res = requests.get("https://en.wikipedia.org/wiki/Grace_Hopper")
soup = bs4.BeautifulSoup(res.text,"lxml")
print(soup)
first_item = soup.select('.vector-toc-text')

for item in soup.select('.vector-toc-text'):
    print(item.text)

print(soup.select('.mw-file-element'))
computer = soup.select('.mw-file-element')[0]
print(computer['src'])
image_link = requests.get("https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Grace_Hopper_being_promoted_to_Commodore.JPEG/330px-Grace_Hopper_being_promoted_to_Commodore.JPEG")
print(image_link)
image_link.content
f = open('my_computer_image.jpg','wb')
f.write(image_link.content)
f.close()