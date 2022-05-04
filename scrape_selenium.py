from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd

#initializing Chrome webdrivers
chromedriver_autoinstaller.install()
driver = webdriver.Chrome(service=Service())

#opening the cvs website
driver.get('https://www.cvs.com')
driver.maximize_window()

#navigating to protein page
shop = driver.find_element(By.XPATH, '//a[text() = "Shop"]')
shop.click()

diet = driver.find_element(By.XPATH, '//div[text() = "Diet & nutrition"]')
diet.click()

protein = driver.find_element(By.XPATH, '//ul[@style = "padding: 13.5px 0px 0px 12px; margin: 0px;"]/li[4]/a')
protein.click()

#scraping the product info
name = driver.find_elements(By.XPATH, '//div[@class = "css-1dbjc4n r-eqz5dr r-156q2ks r-1udh08x"]/section/div')

for x in name:
    print(x.text)

price = driver.find_elements(By.XPATH, '//div[@class = "css-901oao r-1jn44m2 r-evnaw r-b88u0q r-135wba7"]')

for x in price:
    print(x.text)

reviews = driver.find_elements(By.XPATH, '//div[@class = "css-1dbjc4n r-1kihuf0"]')

average = driver.find_elements(By.XPATH, '//div[@class = "css-1dbjc4n r-1awozwy r-18u37iz r-zl2h9q"]/section')

"""
#creating dataframe [DOESNT WORK :(]
product_df = pd.DataFrame(columns = ['Product Name', 'Price', 'Reviews', 'Average Reviews'])

for x in range(len(name)):
    product_df = product_df.append({
        'Product Name' : name[x].text,
        'Price': price[x].text,
        'Reviews': reviews[x].text,
        'Average Revoews' : average[x].text})

print(product_df)
"""