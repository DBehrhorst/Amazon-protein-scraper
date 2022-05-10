"""Scrape Amazon website for all protien supplement data"""
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd

#implementation of Scrape_Protein class - uses webscraping to obtain protein supplement information
class scrape_proteins:
    df = None
    def __init__(self):
        pass

    #defining the webscrape function
    """
    uses the Amazon website to scrape protein supplements
        -obtains protein product links
        -finds the product name, price, info, and review
        -prints information into a dataframe
    """
    def webscrape(self):
        links = []

        #looping through the pages to find product links and appending to link list
        for x in range (1,2):
            url = (f"https://www.amazon.com/s?i=hpc&bbn=3760901&rh=n%3A6973704011&fs=true&page=2&qid=1651897576&ref=sr_pg_{x}")
            
            #initializing drivers
            chromedriver_autoinstaller.install()
            driver = webdriver.Chrome(service=Service())
            driver.get(url)

            #finding the product links using XPATH
            products = driver.find_elements(By.XPATH, '//a[@class = "a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]')

            #appending the product links using XPATH
            for y in products:
                hrefs = y.get_attribute("href")
                links.append(hrefs)

        #looping through link list to find and print product information (name, price, info, and average reviews)
        names = []
        prices = []
        reviews = []
        averages = []
        for link in links:
            driver.get(link)

            #finding the product information using XPATH
            name = driver.find_elements(By.XPATH, '//h1[@class = "a-size-large a-spacing-none"]/span')
            price = driver.find_elements(By.XPATH, '//div[@id = "corePrice_feature_div"]/div/span/span[2]')
            review = driver.find_elements(By.XPATH, '//div[@class = "centerColAlign centerColAlign-bbcxoverride"]/div/div/span[3]/a/span')
            average = driver.find_elements(By.XPATH, '//div[@class = "a-fixed-left-grid-col aok-align-center a-col-right"]/div/span/span')

        #appending the products to a dataframe
            for n in name:
                names.append(n.text)
            
            for p in price:
                prices.append(p.text)

            for r in review:
                reviews.append(r.text)

            for a in average:
                averages.append(a.text)
        d = {
            'Product Name' : names,
            'Price' : prices,
            'Reviews' : reviews,
            'Average Rating' : averages
        }
        df = pd.DataFrame(data = d)
        df[df.columns] = df[df.columns].replace({'\$':''}, regex = True)
        df[df.columns] = df[df.columns].replace({'\n':'.'}, regex = True)
        df['Price'] = df['Price'].astype(float)

        return df

#defining the sorting function
"""
uses the dataframe to sort through various options based on the users request
    -Lowest to Highest Price
    -Highest to Lowest Price
    -Highest to Lowest Average Reviews
"""
def sort():
    scraped_proteins = scrape_proteins()
    data = scrape_proteins.df

    #obtaining the user input for specified sorting
    print("""
    Options to sort include:
        1. Lowest to Higest Price
        2. Highest to Lowest Price
        3. Highest to Lowest Average Reviews
    """)
    sorting = input('Among these choices, which option would you like to choose? (Input one numerical value): ')

    #sorting the dataframe based on the user input
    if sorting == '1':
        data.sort_values(by = 'Price', ascending = True)
        print(data)
    elif sorting == '2':
        data.sort_values(by = 'Price', ascending = False)
        print(data)
    elif sorting == '3':
        data.sort_values(by = 'Average Reviews', ascending = False)
        print(data)

#defining the price input function
"""
printing out specified price ranges based on user input
"""
def price():
    scraped_proteins = scrape_proteins()
    data = scrape_proteins.df

    #user input for their price range
    low = input('Specify your low price point (Input one numerical value): ')
    high = input('Specify your high price point (Input one numerical value: ')

    #outputting prices specified in their range
    data.drop(data[data.Price < float(low)].index, inplace = True)
    data.drop(data[data.Price > float(high)].index, inplace = True)

#defining the if__name__ == "__main__ function"
if __name__ == "__main__":
    x = scrape_proteins()
    x.webscrape()

    print("""
    Welcome to the Amazon Protein Scraper! Options for this program include:

    1. View full database
    2. Sort products
    3. Filter for specified price range
    """)
    option = input('Select the option you would like (Input one numerical value): ')
    
    if option == '1':
        print(x.df)
    elif option == '2':
        sort()
    elif option == '3':
        price()

