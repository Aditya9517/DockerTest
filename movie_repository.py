import json
import time
import warnings
from utils import initialize_browser
from bs4 import BeautifulSoup

# from webdriver_manager.chrome import ChromeDriverManager
warnings.simplefilter(action='ignore', category=UserWarning)


class MovieRepository:

    def __init__(self):
        self.browser = initialize_browser()

        # resulting dataset after pre-processing
        self.imdb_data = {}

        # search_url
        self.search_url = "https://www.imdb.com/find?q="

        # movie url
        self.movie_url = "https://www.imdb.com/title/{0}/reviews"

    def movie_information_repository(self, name):
        movie_url = self.search_url + name
        self.browser.get(movie_url)
        page_source = self.browser.page_source

        soup = BeautifulSoup(page_source, 'html.parser')
        link = soup.find('table').find('tbody').find('tr').find_all(href=True)
        movie_uid = str(link[0]).split('>')[0].split('=')[1].split('/')[2]



        # closes Google Chrome after processing has been completed
        self.browser.close()
        return self.movie_url.format(movie_uid)
