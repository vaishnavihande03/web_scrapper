import requests
from bs4 import BeautifulSoup
webpage=requests.get("https://www.webscraper.io/test-sites/e-commerce/static/computers")
#print(type(webpage.text))
print(webpage.text)
result=BeautifulSoup(webpage.text,"html.parser")
print(result.head)
print(result.body)
print(result.h2)
print(result.h4)
print(result.title)

#prettify fun used aranged text proper format
print(result.body.prettify())
print(result.head.prettify())

#attrs used to display attributes
print(result. html.attrs)
print(result.header.attrs)
print(result.header['role'])
print(result.header['class'])
header=result.header['role']='abc'
print(header)
print(result.header.attrs)
header=result.header['new']='python'
print(result.header.attrs)
#header=del result.header['new']
print(header)
print(result.header.button)

#find func
print(result.find("div").prettify())
print(result.find("title").prettify())

#find all func
print(result.find_all("h1"))
print(len(result.find_all("h1")))