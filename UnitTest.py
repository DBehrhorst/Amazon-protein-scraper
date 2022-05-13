import unittest
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd

#implemention of AmazonTest class - finding the links to products from main protein page
class AmazonTestCase(unittest.TestCase):
    main = 'https://www.amazon.com/s?bbn=3760901&rh=n%3A6973704011&fs=true&ref=lp_6973704011_sar'
    product = 'https://www.amazon.com/Dymatize-Hydrolyzed-Absorbing-Digesting-Servings/dp/B099HZG89P/ref=sr_1_12?qid=1652420758&rdc=1&s=hpc&sr=1-12'
    
    #implementation of test_main_product_page function - 
    def test_main_product_page(self):

        #initializing webdrivers
        chromedriver_autoinstaller.install()
        self.driver = webdriver.Chrome(service=Service())

        #opening main products page
        self.driver.get(self.main)

        #searching for product links in the main products page
        self.prodlink = self.driver.find_elements(By.XPATH, '//a[@class = "a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]')

        #appending prodlinks to list
        self.links = []
        for y in self.prodlink:
                hrefs = y.get_attribute("href")
                self.links.append(hrefs)

    def test_individual_protein_page(self):

        #initializing webdrivers
        chromedriver_autoinstaller.install()
        self.driver = webdriver.Chrome(service=Service())

        self.driver.get(self.product)

        #searching for product name, price, ratings, and average ratings
        self.name = self.driver.find_elements(By.XPATH, '//h1[@class = "a-size-large a-spacing-none"]/span')
        self.price = self.driver.find_elements(By.XPATH, '//div[@id = "corePrice_feature_div"]/div/span/span[2]')
        self.review = self.driver.find_elements(By.XPATH, '//div[@class = "centerColAlign centerColAlign-bbcxoverride"]/div/div/span[3]/a/span')
        self.average = self.driver.find_elements(By.XPATH, '//div[@class = "a-fixed-left-grid-col aok-align-center a-col-right"]/div/span/span')

        enter_name = self.name[0].text
        try:
            enter_price = self.price[0].text
        except IndexError:
            enter_price = 0 
        enter_review = self.review[0].text
        enter_average = self.average[0].text

        #creating a dictionary containing scraped data
        d = {'Product Name' : enter_name, 'Price' : enter_price, 'Reviews' : enter_review, 'Average Rating' : enter_average}
        
        #appending dictionary to data list
        data = []
        data.append(dict(d))
        
        self.name.clear()
        self.price.clear()
        self.review.clear()
        self.average.clear()
        d.clear()

    
        #appending data list to dataframe
        df = pd.DataFrame(data)

        #removing $ sign from dataframe
        df[df.columns] = df[df.columns].replace({'\$':''}, regex = True)

        #replacing '\n' string with '.'
        df[df.columns] = df[df.columns].replace({'\n':'.'}, regex = True)

        #removing ' out of 5' from average ratings
        df[df.columns] = df[df.columns].replace({' out of 5':''}, regex = True)

        #setting price variables & average ratings to float
        df['Price'] = df['Price'].astype(float)
        df['Average Rating'] = df['Average Rating'].astype(float)

        print(df)
    
if __name__ == '__main__':
    unittest.main()


