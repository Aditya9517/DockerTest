import time
import warnings
from utils import initialize_browser
from bs4 import BeautifulSoup
from json2html import *

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

        self.movie_url = self.movie_url.format(movie_uid)

        return self.movie_url

    def movie_reviews(self, movie_review_url):
        imdb_data = {}
        self.browser.get(movie_review_url)
        while True:
            try:
                # automates the process of load more button to obtain all the reviews
                button = self.browser.find_element_by_xpath('//*[@id="load-more-trigger"]')
                button.click()
                time.sleep(5)
            # the loop breaks when "load-more" button is not present
            except Exception as e:
                break

        page_source = self.browser.page_source

        # using BeautifulSoup to parse the HTML page
        soup = BeautifulSoup(page_source, "html.parser")

        # initializing value of the movie name
        movie_name = ""

        # searches the HTML page to find related movie name class
        for item in soup.find_all(class_="subpage_title_block"):
            movie_name = str(item.find(class_="parent").text).rstrip('\r\n').lstrip().replace("\n", "").replace(" ", "")

            # key contains the movie name
            imdb_data[movie_name] = []

        # searches the HTML page to find reviews related movie name
        for item in soup.find_all(class_="review-container"):
            title_review = {}
            review_title = item.find(class_="title").text.rstrip()
            review = item.find(class_="text").text.rstrip().replace("\n", " ")
            title_review['title'] = review_title
            title_review['review'] = review

            # creates a list of reviews corresponding to the movie name
            imdb_data[movie_name].append(title_review)

        # # create a JSON file to store the values
        # with open('movie_reviews.json', 'w', encoding="utf-8") as f:
        #     json.dump(imdb_data, f, indent=2, ensure_ascii=False)

        # closes Google Chrome after processing has been completed
        self.browser.close()

        return json2html.convert(json=imdb_data)


if __name__ == '__main__':
    t = MovieRepository()
    print(t.movie_information_repository('tenet'))