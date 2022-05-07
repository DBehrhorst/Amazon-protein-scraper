"""Scrape CVS website for all protien supplement data"""
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pandas as pd

#implementation of Scrape_Protein class - uses webscraping to obtain protein supplement information
class scrape_proteins:
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
        links = []
        #looping through the 8 pages to find product links and appending to link list
        for x in range (1,8):
            url = "https://www.cvs.com/shop/diet-nutrition/protein?page=" + str(x)
            chromedriver_autoinstaller.install()
            driver = webdriver.Chrome(service=Service())
            time.sleep(5)
            driver.get(url)

            products = driver.find_elements(By.XPATH, '//a[@class = "css-1dbjc4n r-1o9r03r r-1loqt21 r-qtbb1w r-u8s1d r-1wipuzn r-1sofzug r-1otgn73 r-1i6wzkk r-lrvibr"]')

            for y in products:
                hrefs = y.get_attribute("href")
                links.append(url + hrefs)

        #looping through link list to find and print product information (name, price, info, and average reviews)
        product_list = []
        for link in links:
            driver.get(link)
            name = driver.find_elements(By.XPATH, '//h1[@class = "css-4rbku5 css-901oao r-1jn44m2 r-1ui5ee8 r-vw2c0b r-16krg75"]')
            price = driver.find_elements(By.XPATH, '//div[@class = "css-901oao r-1khnkhu r-1jn44m2 r-3i2nvb r-vw2c0b r-1b7u577"]')
            reviews = driver.find_elements(By.XPATH, '//div[@class = "css-901oao r-1khnkhu r-ubezar"]')
            average = driver.find_elements(By.XPATH, '//div[@class = "css-901oao r-suhe1l r-vw2c0b r-7o8qx1"]')

            for n in name:
                product_list.append(n.text)
            
            for p in price:
                product_list.append(p.text)

            for r in reviews:
                product_list.append(r.text)

            for a in average:
                product_list.append(a.text)
            time.sleep(10)

        print(product_list)


#defining the if__name__ == "__main__ function"
if __name__ == "__main__":        
    x = scrape_proteins()
    x.webscrape()
