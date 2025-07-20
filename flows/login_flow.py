from pages.home_page import HomePage
from pages.login_page import LoginPage
from infra.data_loader import DataLoader


class LoginFlow:
    def __init__(self, driver):
        self.driver = driver
        self.home_page = HomePage(driver)

    def navigate_to_login_page(self):
        self.home_page.open()
        self.home_page.navigate_to_login()
        return self  # chaining enabled


class LoginFlow:
    def __init__(self, driver):
        self.driver = driver
        self.home_page = HomePage(driver)
        self.login_page = LoginPage(driver)

    def login_to_portal(self, contact):
        self.home_page.open()
        self.home_page.navigate_to_login()
        print("URL before click_password_login_link:", self.driver.current_url)
        print("HTML snapshot:")
        print(self.driver.page_source[:3000])  # print first 3000 characters only to avoid overflow

        self.login_page.click_password_login_link()
        
        self.login_page.enter_username(contact["username"])
        self.login_page.enter_password(contact["password"])
        self.login_page.click_login()
        return self
