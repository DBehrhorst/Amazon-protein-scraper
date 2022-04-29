"""Scrape CVS website for all protien supplement data"""
import requests
import http.client
import pandas as pd
from bs4 import BeautifulSoup

http.client._MAXHEADERS = 1000
#implementation of Scrape_Protein class - uses webscraping to obtain protein supplement information
class ScrapeInfo:
    def __init__(self):
        pass

    #defining the webscrape function
    """
    uses the CVS website to scrape protein supplements
        -obtains protein product links
        -finds the product name, price, info, and review
        -prints information into a dictionary

    """

    def webscrape(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
        url = 'https://www.cvs.com'

        links = []

        #looping through the 8 pages and appending to a links list
        for x in range(1,8):
            r = requests.get(f'https://www.cvs.com/shop/diet-nutrition/protein?page={x}')
            bsoup = BeautifulSoup(r.content, 'lxml')

            products = bsoup.find_all('div', class_ ='css-1dbjc4n r-1pi2tsx' )

            for product in products:
                for link in product.find_all('a', href = True):
                    links.append(url + link['href'])

        #looping through link list to find and print product name, price, info, and average reviews
        for link in links:
            r = requests.get(link, headers = headers)
            bsoup = BeautifulSoup(r.content, 'lxml')

            prod_name = bsoup.find('h1', class_ = 'css-4rbku5 css-901oao r-1jn44m2 r-1ui5ee8 r-vw2c0b r-16krg75')
            prod_price = bsoup.find('div', class_ = 'css-901oao r-1khnkhu r-1jn44m2 r-3i2nvb r-vw2c0b r-1b7u577')
            prod_info = bsoup.find('div', class_ = 'css-901oao r-1jn44m2 r-1enofrn')
            prod_review = bsoup.find('div', class_ = 'css-901oao r-jw6ls8 r-1enofrn r-b88u0q r-m2pi6t')

            proteins = {
                'Product' : prod_name,
                'Price' : prod_price,
                'Info' : prod_info,
                'Average Rating' : prod_review
            }
            print(proteins)
        
#defining the if__name__ == "__main__ function"
if __name__ == "__main__":        
    x = ScrapeInfo()
    x.webscrape()