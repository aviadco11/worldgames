from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Utils import *


def test_scores_service(url):
    driver = webdriver.Firefox()
    driver.get(url)
    score = driver.find_element(by="id", value="score")
    if 1 <= int(score.text) <= 1000:
        return True
    else:
        return False


def main_function():
    if test_scores_service(Utils.URL_TEST):
        print("score between 1 to 1000")
        return 0
    else:
        print("score not in the range 1..1000")
        return -1


main_function()
