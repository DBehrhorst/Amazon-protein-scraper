"""Scrape CVS website for all protien supplement data"""
import requests
from bs4 import BeautifulSoup

class ScrapeInfo:
    """scraper object """
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
        self.url = 'https://www.cvs.com/'
    def scraper():
        r = requests.get('https://www.cvs.com/shop/diet-nutrition/protein?icid=shop-diet-cat-link3-protein%27')
        bsoup = BeautifulSoup(r.content, 'lxml')
        links = soup.find_all('div,' class_ = )

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
