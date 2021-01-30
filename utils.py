from selenium import webdriver


def initialize_browser():
    # chrome driver used by selenium
    # browser = webdriver.Chrome(ChromeDriverManager().install())
    browser = webdriver.PhantomJS("phantomjs-2.1.1-macosx/bin/phantomjs")
    return browser