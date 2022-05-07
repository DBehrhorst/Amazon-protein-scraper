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
        for x in range (1,30):
            url = (f"https://www.amazon.com/s?i=hpc&bbn=3760901&rh=n%3A6973704011&fs=true&page=2&qid=1651897576&ref=sr_pg_{x}")
            chromedriver_autoinstaller.install()
            driver = webdriver.Chrome(service=Service())
            driver.get(url)

            products = driver.find_elements(By.XPATH, '//a[@class = "a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]')

            for y in products:
                hrefs = y.get_attribute("href")
                links.append(hrefs)

        #looping through link list to find and print product information (name, price, info, and average reviews)
        product_list = []
        for link in links:
            driver.get(link)
            name = driver.find_elements(By.XPATH, '//h1[@class = "a-size-large a-spacing-none"]/span')
            price = driver.find_elements(By.XPATH, '//td[@class = "a-span12"]/span/span')

            for n in name:
                product_list.append(n.text)
            
            for p in price:
                product_list.append(p.text)

        print(product_list)

#defining the if__name__ == "__main__ function"
if __name__ == "__main__":        
    x = scrape_proteins()
    x.webscrape()
