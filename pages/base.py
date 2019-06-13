from selenium.webdriver.common.by import By
from pages.page import Page

class Base(Page):
    _dialog_title_locator = (By.CSS_SELECTOR, '.popup-signup > h3')  # Added this locator for dialog_close
    _dialog_close_locator = (By.CSS_SELECTOR, '.ui-dialog .ui-dialog-titlebar .ui-button .close-btn-new')  # Added this locator for dialog_close

