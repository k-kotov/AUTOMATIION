from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://demoblaze.com/index.html")

    def click_s6(self):
        s6 = self.driver.find_element(By.XPATH, value='//a[text()="Samsung galaxy s6"]')
        s6.click()

    def click_monitor_test(self):
        monitor = self.driver.find_element(By.CSS_SELECTOR, value='''[onclick="byCat('monitor')"]''')
        monitor.click()

    def count_test(self, count):
        monit = self.driver.find_elements(By.CSS_SELECTOR, value='.card')
        assert len(monit) == count