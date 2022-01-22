from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_running_autotests_for_different_interface_languages(browser):
    result = search_button(browser)
    # time.sleep(30)
    if not result:
        assert False, "!!Кнопка не найдена!!"
    else:
        assert True, "!!Кнопка присутствует на странице. Все ОК!!"


def search_button(browser):
    browser.get(link)
    try:
        browser.find_element(By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")
    except NoSuchElementException:
        return False
    return True
