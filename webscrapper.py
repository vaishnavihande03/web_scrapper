import random
import pandas
import datetime
import openpyxl
import requests
from bs4 import BeautifulSoup

#provide the link
inp=input("enter the link here:")
print(inp)
webpage=(requests.get(inp))
content=webpage.content
result=BeautifulSoup(content,'html.parser')

#enter the product common tag here:
products_common_tag=input("enter the Products Common Tag here:")
products=result.find_all("div",{"class":products_common_tag}) #product class

#create the list
names=[]
prices=[]
links=[]
print("Total Products:", len(products))

#give the input tag for name,price and links
tag_input = input("Enter the product naming tag: ")
product_tag = input("enter the tag for price:")
product_link = input("enter the tag for product link:")


for product in products:
    product_name_tag = product.find('a', {"class":tag_input} )
    product_pricc_tag = product.find('span',{"class":product_tag})
    product_pricc_image = product.find('div',{"class":product_link})

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

# Use zip function
data=list(zip(names,prices,links))
print(data)

#to display data in proper format
d=pandas.DataFrame(data)

# Generate a timestamp to include in the file name
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

# Concatenate the timestamp with the file name
file_name = f"data_{timestamp}.xlsx"
try:
    d.to_excel(file_name)
except:
    print("something is wrong")
else:
    print("scuccesfull")
finally:
      print("hello")