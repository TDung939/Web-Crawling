from bs4 import BeautifulSoup
import requests
import pandas as pd

url = input()
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

products = soup.findAll('div', {'class':"product-item"})

#Needed info
seller_id = []
product_id = []
title = []
price = []
img_url = []

#Extracting info
for product in products:
    product_id.append(product["data-id"])
    seller_id.append(product["data-seller-product-id"])
    title.append(product["data-title"])
    price.append(product["data-price"])
    images = product.find('img',{'class':'product-image img-responsive'}); img_url.append(images["src"])

data = {
    'product_id': product_id,
    'seller_id': seller_id,
    'title': title,
    'price': price,
    'img_url': img_url
}

pd.set_option('display.max_columns', None)
dataFrame = pd.DataFrame(data=data)
print(dataFrame)