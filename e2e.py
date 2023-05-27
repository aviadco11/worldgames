from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import Utils


def test_scores_service(url):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    score = driver.find_element(by="id", value="score")
    if 1 <= int(score.text) <= 1000:
        return True
    else:
        return False


def main_function():
    if test_scores_service(Utils.URL_TEST):
        return 0
    else:
        return -1



