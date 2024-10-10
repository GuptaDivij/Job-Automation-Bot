from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
from bs4 import BeautifulSoup
from config import PREFERENCES

def login(driver):
    driver.get("https://www.glassdoor.com/index.htm")
    print("Please log in to Glassdoor manually...")
    while True:
        try:
            WebDriverWait(driver, 2).until(EC.url_contains("member"))
            break
        except TimeoutException:
            pass
    print("Logged in successfully.")

def search_jobs(driver):
    driver.get("https://www.glassdoor.com/Job/jobs.html")
    time.sleep(2)
    try:
        # Enter job preferences
        driver.find_element(By.ID, "sc.keyword").send_keys(PREFERENCES['position_title'])
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        print(f"Searching for jobs: {PREFERENCES['position_title']}")
    except NoSuchElementException:
        print("Error in searching jobs.")
        
def get_job_links(driver):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='MainCol']/div[1]/ul")))
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    job_links = [f"https://www.glassdoor.com{link['href']}" for link in soup.find_all('a', {"class": "jobLink"})]
    return set(job_links)

def scrape_jobs():
    driver = webdriver.Chrome()
    login(driver)
    search_jobs(driver)
    job_links = get_job_links(driver)
    driver.quit()
    print(f"Found {len(job_links)} job links.")
    return job_links

if __name__ == "__main__":
    scrape_jobs()
