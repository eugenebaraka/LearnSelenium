from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install())

url = 'https://chromedriver.storage.googleapis.com/index.html'
driver.implicitly_wait(30) # clicks until the element below (ID) is available,
# going to be set as a default wait across the script even if we don't specify it any more

driver.get(url)
driver.find_element(By.ID, "downloadButton").click()

WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element(
        # Element filtration
        (By.CLASS_NAME, 'progress-label'),
        'Complete!' # Expected text

    )
)

