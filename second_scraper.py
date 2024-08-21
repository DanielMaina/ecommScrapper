import requests
from bs4 import BeautifulSoup
import pandas as pd

baseurl = 'https://www.2ndstreet.jp'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

productlinks = []

for x in range(90,100):
    r = requests.get(f'https://www.2ndstreet.jp/search?category=910001&page={x}')
    soup = BeautifulSoup(r.content, 'html.parser')
    productlist = soup.find_all('li', class_='js-favorite')
    for item in productlist:
        for link in item.find_all('a', href=True):
            productlinks.append(baseurl + link['href'])


# testlink = 'https://www.2ndstreet.jp/goods/detail/goodsId/2336860433855/shopsId/31181'

driplist = []
for link in productlinks:
    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')  
    
    try:
        name = soup.find('div', class_='productName -backorder').text.strip()
    except:
        name = 'no name'

    try:
        brand = soup.find('div', class_='blandName').text.strip()
    except:
        brand = 'no brand'

    try:
        price = soup.find('span', class_='priceNum').text.strip()
    except:
        price = 'no price'

    try:
        description = soup.find('div', class_='conditionStatus').text.strip()
    except:
        description = 'no description'

    try:
        getimage = soup.find('a', class_='expandImageBtn').find("img")
        fimage = getimage['data-src']
    except:
        image = 'no image'
    try:
        # getPimage = []
        # getsecondary = soup.find('li', class_='slick-slide thumbnail-item') 
        # for pimage in getsecondary:            
        #     pimage = getPimage['data-src']
        #     getPimage.append(pimage)   
        getsecondimage = soup.find('li', class_='slick-slide thumbnail-item').find("img")          
        secondimage = getsecondimage['data-src']
    except:
        pimage = 'no secondary image'

    
    drip = {
        'brand': brand,
        'name': name,    
        'price': price,
        'description': description,
        'image': fimage,
        'secondary image': secondimage
        }

    driplist.append(drip)
    print('Saving: ', drip)

df = pd.DataFrame(driplist)

df.to_csv('2ndstreet_v3_2.csv')



    




# name, brand, price, image, description, size(jap), catagory(jap)

# print(soup.find('div', class_='blandName').text.strip())




# https://www.2ndstreet.jp/store

# https://www.2ndstreet.jp/search?category=910001

# https://www.2ndstreet.jp/search?category=910001&page=2