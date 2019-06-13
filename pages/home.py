from pages.base import Base
from selenium.webdriver.common.by import By

class Home(Base):
    _header_shop_button_locator = (By.CSS_SELECTOR, ".home-main > div > a")

    def verify_header_shop_button(self):
        self.selenium.find_element(*self._header_shop_button_locator).click()