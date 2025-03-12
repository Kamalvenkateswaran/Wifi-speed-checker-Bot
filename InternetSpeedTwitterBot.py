from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


class InternetSpeedTwitterBot:
    def __init__(self):
        self.TWITTER_EMAIL = 'kamal.100daysofcode@gmail.com'
        self.TWITTER_PASSWORD ='100Daysofcode'
        self.TWITTER_USERNAME="@kamalv31037"
        self.driver = None  # Initialize WebDriver as None
        self.driver_2 = None

    def get_speed(self):
        """Fetches download and upload speeds."""
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://www.speedtest.net/")
        go = self.driver.find_element(By.CLASS_NAME, value='start-text')
        go.click()
        if self.driver is None:
            print("Error: Browser is not open. Run `start()` first.")
            return

        time.sleep(60)  # Wait for test to complete
        self.down = self.driver.find_element(By.CSS_SELECTOR, ".download-speed")
        self.down=self.down.text
        self.down=float(self.down)
        # print(f"The download speed is {self.down} Mbps")

        self.up = self.driver.find_element(By.CSS_SELECTOR, ".upload-speed")
        self.up = self.up.text
        self.up = float(self.up)
        # print(f"The upload speed is {self.up} Mbps")
        self.driver.close()

    def twitter(self):
        """Logs into Twitter (X.com) to post speed results."""
        self.driver_2 = webdriver.Chrome(options=chrome_options)
        self.driver_2.get("https://x.com/i/flow/login")
        wait = WebDriverWait(self.driver_2, 15)

        time.sleep(20)  # Wait for page to load

        email = self.driver_2.find_element(By.CSS_SELECTOR, value='.r-fdjqy7')
        email.send_keys(self.TWITTER_EMAIL)
        email.send_keys(Keys.ENTER)

        time.sleep(3)
        username=self.driver_2.find_element(By.CSS_SELECTOR,value='.r-fdjqy7')
        username.send_keys(self.TWITTER_USERNAME)
        username.send_keys(Keys.ENTER)


        password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))

        # Scroll into view in case it's hidden
        self.driver_2.execute_script("arguments[0].scrollIntoView();", password_input)

        password_input.send_keys(self.TWITTER_PASSWORD)
        password_input.send_keys(Keys.ENTER)

        tweet_box = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[role="textbox"]')))
        tweet_box.send_keys(f"Hey Internet Provider, why is my internet speed {self.down} down/{self.up}up when I pay for {100}down/{50}up?")

        time.sleep(3)
        tweet_box.send_keys(Keys.CONTROL,Keys.ENTER)








