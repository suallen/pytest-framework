from pages.home import Home
import sys, os; sys.path.insert(0, os.path.abspath('..'));

def test_verify_click_header_shop_now(base_url_live, driver):
    home_page = Home(base_url_live, driver).open()
    home_page.verify_header_shop_button()
    print("success")