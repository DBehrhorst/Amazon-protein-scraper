"""Scrape CVS website for all protien supplement data"""
import requests
from bs4 import BeautifulSoup

url = 'https://www.cvs.com/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}

r = requests.get('https://www.cvs.com/shop/diet-nutrition/protein?icid=shop-diet-cat-link3-protein%27')

class ScrapeInfo:
    """scraper object """
    def __init__(self, html):
        self.name = scrapeName(html)
        self.price = scrapePrice(html)
        self.avgRating = scrapeAvgRating(html)
        self.numReview = scrapeNumReview(html)

def scrapeName(html):
    """scrapes product name"""
    pass
def scrapePrice(html):
    """scrapes product price"""
    pass
def scrapeAvgRating(html):
    """scrapes average product rating"""
    pass
def scrapeNumReview(html)
    """scrapes number of product reviews"""
    pass




def main():
    pass

if __name__ == "__main__":
    pass