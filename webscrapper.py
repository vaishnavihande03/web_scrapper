import random

import pandas
import openpyxl
import requests
from bs4 import BeautifulSoup
inp=input("enter the link here:") #amazon link
print(inp)
webpage=(requests.get(inp))
content=webpage.content

result=BeautifulSoup(content,'html.parser')
# print(result.html.attrs)
#print(result.prettify())
#print(result.title.prettify())
products_common_tag=input("enter the Products Common Tag here:") #amazon link
products=result.find_all("div",{"class":products_common_tag}) #product class
#print(products[0].div.string) #price

names=[]
prices=[]
links=[]
print("Total Products:", len(products))
for product in products:
    # print(product)
    product_name_tag = product.find('a', class_='search_Ptitle')
    product_pricc_tag = product.find('span',class_='search_PSellingP')
    product_pricc_image = product.find('div',class_='pro-buck-img')
    if product_name_tag:
        product_name = product_name_tag.text.strip()
        print("Product Name:", product_name)
        names.append(product_name)
    else:
        print("Product Name Not Available")
        names.append("NA")

    if product_pricc_tag:
        product_price = product_pricc_tag.text.strip()
        print("Product Price:", product_price)
        prices.append(product_price)
    else:
        print("Product Price Not Available")
        prices.append("NA")

    if product_pricc_image:
        product_image_link = product_pricc_image.a['href']
        print("Product Image:", product_image_link)
        links.append(product_image_link)
    else:
        print("Product Link Not Available")
        links.append("NA")
    # product_name_tag = product.div.div
    # print(product_name_tag)
# print(len(products))
"""
products = result.find_all('id', {'id':"ctl00_ContentPlaceHolder1_divSearchData")

for product_div in product_divs:
    
product_price_tag = product_div.find('span', class_='search_PSellingP')

if product_name_tag and product_price_tag:
    product_name = product_name_tag.text.strip()
product_price = product_price_tag.text.strip()

print(f"Product Name: {product_name}, Price: {product_price}")
else:
print("Product name or price not found for a product.")
"""
# print(products[0].prettify())
print("product 1")
# name1=products[0].div.div
# print(name1)
#product_tags = products.find_all('a', class_='search_Ptitle linkdisabled')
"""
"""
"""
if product_tags:
    for product_tag in product_tags:
        product_name = product_tag.text.strip()
        print(product_name)
else:
    print("Product tags not found.")
"""
#desired_tag = result.find('a', {'class':'search_Ptitle linkdisabled'})
#print(products[0].a.string)
# Find the desired tag using its class attribute
#desired_tag = result.find('a', {'class'='search_Ptitle linkdisabled')

# Check if the tag was found before accessing its text attribute
#result = desired_tag.text if desired_tag else "Tag not found"

#print(result)
#print(desired_tag.text)
#print(products[1].h4.string)
#print(products[0].div[3].a['title'].string)   #name

#for parent_div in products:
 #   child_a = parent_div.find('a', class_='search_Ptitle')
  #  print(child_a.string)
    #link
# link="https://www.webscraper.io/" + products[0].a['href']
# print(link)
#print(products[0].div.string) #price

# names=[]
# prices=[]
# links=[]
"""
"""
"""
for items in products:
    names.append(items.a.string)
    prices.append(items.h4.string)
    links.append( "https://www.webscraper.io/" + items.a['href'])
"""

data=list(zip(names,prices,links))
print(data)

# d=pandas.DataFrame(data,columns=[names,prices,links])
d=pandas.DataFrame(data)

try:
    d.to_excel("data4.xlsx")
except:
    print("something is wrong")
else:
    print("scuccesfull")
finally:
      print("hello")