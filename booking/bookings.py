from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
# from webdriver_manager.core.utils import ChromeType
import booking.constants as const
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Booking:
    def __init__(self, browser = 'Chrome', close_browser = False):
        self.browser = browser
        self.driver = self._load_browser()
        self.close_browser = close_browser
        self.driver.implicitly_wait(60)
        self.driver.maximize_window()

    def _load_browser(self):
        driver = None

        if self.browser == 'Chrome':
            driver = webdriver.Chrome(ChromeDriverManager().install())
        elif self.browser == 'Firefox':
            driver = webdriver.Firefox(GeckoDriverManager().install())
        else:
            print("Webdriver should either be 'Chrome' or 'Firefox'")
        return driver

    def __enter__(self):
        return self

    # def __exit__(self, exc_type, exc_val, exc_tb):
    #     if self.close_browser:
    #         self.driver.quit()

    def land_first_page(self):
        return self.driver.get(const.BASE_URL)

    def change_currency(self, currency = None):
        self.land_first_page()

        currency_element = self.driver.find_element(By.CSS_SELECTOR, 'button[data-testid="header-currency-picker-trigger"]')
        self.driver.execute_script("arguments[0].click();", currency_element)

        try:
            close_signup_call = self.driver.find_element(By.CSS_SELECTOR, 'span.b6dc9a9e69.e25355d3ee')
            close_signup_call.click()
        finally:
            print("No call to sign up found. Skipping...")



        selected_currency_element = f'//button[contains(.//div, "USD")]'
        self.driver.execute_script("arguments[0].click();", selected_currency_element)

        #
        # WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(
        #     (By.XPATH, selected_currency_element)
        # )).click()







