from selenium import webdriver
from utils import apply_to_greenhouse, apply_to_lever
from job_scraper import scrape_jobs
import time

def apply_to_jobs(job_links):
    driver = webdriver.Chrome()

    for url in job_links:
        print(f"Applying to job: {url}")
        driver.get(url)

        if 'greenhouse' in url:
            apply_to_greenhouse(driver)
        elif 'lever' in url:
            apply_to_lever(driver)
        else:
            print(f"Unknown platform for {url}")

        time.sleep(5)  # Pause to avoid being flagged as a bot

    driver.quit()

if __name__ == "__main__":
    job_links = scrape_jobs()
    apply_to_jobs(job_links)
