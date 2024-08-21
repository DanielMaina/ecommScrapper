import requests
from bs4 import BeautifulSoup
import pandas as pd

baseurl = 'https://poshmark.ca'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

productlinks = []

for x in range(1,3):
    r = requests.get(f'https://poshmark.ca/category/Men?max_id={x}')
    soup = BeautifulSoup(r.content, 'html.parser')
    productlist = soup.find_all('div', class_='col-x12 col-l6 col-s8 p--2')
    for item in productlist:
        for link in item.find_all('a', href=True):
            productlinks.append(baseurl + link['href'])


# testlink = 'https://poshmark.ca/listing/MBX-novelty-hot-sauce-print-button-down-shirt-62d062a44578a1d109c20761'

driplist = []
for link in productlinks:
    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')  
    
    try:
        name = soup.find('h1', class_='fw--light m--r--2 listing__title-container').text.strip()
    except:
        name = 'no name'

    try:
        getbrand = soup.find('div', class_='listing__title').find("a")
        brand = getbrand['href']
    except:
        brand = 'no brand'

    try:
        price = soup.find('p', class_='h1').text.strip()
    except:
        price = 'no price'

    try:
        description = soup.find('div', class_='listing__description fw--light').text.strip()
    except:
        description = 'no description'

    try:
        getimage = soup.find('div', class_='img__container img__container--square').find("img")
        image = getimage['src']
    except:
        image = 'no image'

    
    drip = {
        'brand': brand,
        'name': name,    
        'price': price,
        'description': description,
        'image': image
        }

    driplist.append(drip)
    print('Saving: ', drip)


df = pd.DataFrame(productlinks)

df.to_csv('poshmark_2.csv')

# NEED TO FINISH: printing double data set




# # testlink = 'https://www.2ndstreet.jp/goods/detail/goodsId/2336860433855/shopsId/31181'

# driplist = []
# for link in productlinks:
#     r = requests.get(link, headers=headers)
#     soup = BeautifulSoup(r.content, 'html.parser')  
    
#     try:
#         name = soup.find('div', class_='productName -backorder').text.strip()
#     except:
#         name = 'no name'

#     try:
#         brand = soup.find('div', class_='blandName').text.strip()
#     except:
#         brand = 'no brand'

#     try:
#         price = soup.find('span', class_='priceNum').text.strip()
#     except:
#         price = 'no price'

#     try:
#         description = soup.find('div', class_='conditionStatus').text.strip()
#     except:
#         description = 'no description'

#     try:
#         getimage = soup.find('a', class_='expandImageBtn').find("img")
#         image = getimage['data-src']
#     except:
#         image = 'no image'

    
#     drip = {
#         'brand': brand,
#         'name': name,    
#         'price': price,
#         'description': description,
#         'image': image
#         }

#     driplist.append(drip)
#     # print('Saving: ', drip)

# df = pd.DataFrame(driplist)

# df.to_csv('2ndstreet_v3.csv')



    




# name, brand, price, image, description, size(jap), catagory(jap)

# print(soup.find('div', class_='blandName').text.strip())




# https://www.2ndstreet.jp/store

# https://www.2ndstreet.jp/search?category=910001

# https://www.2ndstreet.jp/search?category=910001&page=2