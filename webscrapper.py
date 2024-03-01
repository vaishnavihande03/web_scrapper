import pandas
import openpyxl

import requests
from bs4 import BeautifulSoup
inp=input("enter the link here:")
print(inp)
webpage=(requests.get(inp))
content=webpage.content

result=BeautifulSoup(content,'html.parser')

products=result.find_all("div",{"class":'sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20'})
names=[]
prices=[]
links=[]

#for item in products:
 #   names.append(item.a.string)
  #  prices.append(item.h4.string)
   # links.append("https://www.amazon.in/" + item.a['href'])

print(products[0].prettify())
print(products[0].a.string)
print(products[0].h4.string)
print("https://www.webscraper.io/"+products[0].a['href'])

"""
data=list(zip(names,prices,links))

d=pandas.DataFrame(data,columns=['name','price','link'])

try:
    print("Total Products:", len(data))
    print(d.columns)
    print(d.values)
    d.to_excel("hello/web.xlsx")
except Exception as e:
    print("error",e)
else:
    print("successfully")
finally:
    print("heyy")
"""