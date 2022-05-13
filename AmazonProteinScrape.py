"""Scrape Amazon website for all protien supplement data"""
from tkinter import E
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd

#implementation of Scrape_Protein class - uses webscraping to obtain protein supplement information
class scrape_proteins:
    
    #defining the __init__ class
    def __init__(self):
        self.dataframe = ()
        pass

    #defining the webscrape function
    """
    uses the Amazon website to scrape protein supplements
        -obtains protein product links
        -finds the product name, price, number of ratings, and average ratings
        -appends information to a dataframe
    """
    def webscrape(self):
        links = []

        #looping through the pages to find product links and appending to link list
        for x in range (0,1):
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
        data = []
        
        for link in links:
            driver.get(link)
            #finding the product information using XPATH
            name = driver.find_elements(By.XPATH, '//h1[@class = "a-size-large a-spacing-none"]/span')
            price = driver.find_elements(By.XPATH, '//div[@id = "corePrice_feature_div"]/div/span/span[2]')
            review = driver.find_elements(By.XPATH, '//div[@class = "centerColAlign centerColAlign-bbcxoverride"]/div/div/span[3]/a/span')
            average = driver.find_elements(By.XPATH, '//div[@class = "a-fixed-left-grid-col aok-align-center a-col-right"]/div/span/span')
            
            
            enter_name = name[0].text
            try:
                enter_price = price[0].text
            except IndexError:
                enter_price = 0 
            enter_review = review[0].text
            enter_average = average[0].text

            #creating a dictionary containing scraped data
            d = {'Product Name' : enter_name, 'Price' : enter_price, 'Reviews' : enter_review, 'Average Rating' : enter_average}
            
            #appending dictionary to data list
            data.append(dict(d))
            
            name.clear()
            price.clear()
            review.clear()
            average.clear()
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
        
        self.dataframe = df
        return df

#defining the sorting function
"""
uses the dataframe to sort through various options based on the users request
    -Lowest to Highest Price
    -Highest to Lowest Price
    -Highest to Lowest Average Reviews
"""
def sort(data):

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
        data.sort_values(by = 'Price', ascending = True, inplace = True)
        print(data)
    elif sorting == '2':
        data.sort_values(by = 'Price', ascending = False, inplace = True)
        print(data)
    elif sorting == '3':
        data.sort_values(by = 'Average Rating', ascending = False, inplace = True)
        print(data)

#defining the price input function
"""
printing out specified price ranges based on user input
"""
def price(data):

    #user input for their price range
    low = input('Specify your low price point (Input one numerical value): ')
    high = input('Specify your high price point (Input one numerical value: ')

    #outputting prices specified in their range
    trimmed = data.drop(data[data.Price < float(low)].index, inplace = False)
    trimmed = data.drop(data[data.Price > float(high)].index, inplace = False)
    print(trimmed)

#defining the search function
def search(data):

    #user input for search keyword
    searching = input('Specify a keyword to search through product names: ')

    #finding and printing the partial match in product name
    x = data[data['Product Name'].str.contains(searching)]
    print(x)

#defining the if__name__ == "__main__ function"
if __name__ == "__main__":

    #calling the instance of the scrape_proteins class
    x = scrape_proteins()

    #calling the webscrape function in class
    x.webscrape()

    #user input for program options
    while True:
        print("""
        ---------------------------------------------------------------------------------      
            
        Welcome to the Amazon Protein Scraper! Options for this program include:
            1. View the full database
            2. Sort products
            3. Filter for specified price range
            4. Search by keyword
            5. Quit
        """)
        option = input('Select the option you would like (Input one numerical value): ')
        
        #option 1: viewing the full database by printing
        if option == '1':
            print(x.dataframe)

        #option 2: sorting the database by calling the sort function
        elif option == '2':
            sort(x.dataframe)

        #option 3: filtering price information by calling the price function
        elif option == '3':
            price(x.dataframe)

        #option 4: searching for keyword by calling the search function
        elif option == '4':
            search(x.dataframe)

        #option 5: allowing the user to quit
        elif option == '5':
            break
