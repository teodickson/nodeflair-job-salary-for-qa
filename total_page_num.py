from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class Page:

    def __init__(self) -> None:
        pass

    def get_page_num(self):
        base_page_url = "https://nodeflair.com/salaries?page=1&user_submitted_only=false&positions%5B%5D=qa_engineer"
        page_num = 0
        page_num_xpath = "(//div[@class='salaries-container__page-nav']//div/b[2])[1]"
        options = Options()
        options.headless = True


        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        driver.get(base_page_url)
        try:
            WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH, page_num_xpath))
            )

            pages = driver.find_element_by_xpath(page_num_xpath)
            page_num = int(pages.text)
        finally:
            driver.quit()
        print("page number is ", page_num)
        return page_num

    #if __name__=="__main__":
        #get_page_num()

