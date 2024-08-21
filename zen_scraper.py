import requests
from bs4 import BeautifulSoup
import pandas as pd

baseurl = 'https://zenmarket.jp/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

r = requests.get('https://zenmarket.jp/yahoo.aspx?c=23000')

soup = BeautifulSoup(r.content, 'html.parser')

productlist = soup.find_all('div', id='yahoo-search-results')

productlinks = []

for item in productlist:
    for link in item.find_all('a', href=True):
        print(link['href'])


## HOW TO: USE BEAUTIFUL SOUP WHEN THE URL CHANGES






# productlinks = []

# for x in range(1,11):
#     r = requests.get(f'https://www.2ndstreet.jp/search?category=910001&page={x}')
#     soup = BeautifulSoup(r.content, 'html.parser')
#     productlist = soup.find_all('li', class_='js-favorite')
#     for item in productlist:
#         for link in item.find_all('a', href=True):
#             productlinks.append(baseurl + link['href'])


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

# df.to_csv('zenmarket.csv')
 



# name, brand, price, image, description, size(jap), catagory(jap)

# print(soup.find('div', class_='blandName').text.strip())




# https://zenmarket.jp/yahoo.aspx?c=23000

# https://zenmarket.jp/auction.aspx?itemCode=t1054355117