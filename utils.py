from config import JOB_APP
import os

def apply_to_greenhouse(driver):
    try:
        driver.find_element_by_id('first_name').send_keys(JOB_APP['first_name'])
        driver.find_element_by_id('last_name').send_keys(JOB_APP['last_name'])
        driver.find_element_by_id('email').send_keys(JOB_APP['email'])
        driver.find_element_by_id('phone').send_keys(JOB_APP['phone'])

        # Upload Resume
        resume_upload = driver.find_element_by_name('resume')
        resume_upload.send_keys(os.path.join(os.getcwd(), JOB_APP['resume']))
        print("Application submitted on Greenhouse.")
    except Exception as e:
        print(f"Failed to apply on Greenhouse: {e}")

def apply_to_lever(driver):
    try:
        driver.find_element_by_name('name').send_keys(f"{JOB_APP['first_name']} {JOB_APP['last_name']}")
        driver.find_element_by_name('email').send_keys(JOB_APP['email'])
        driver.find_element_by_name('phone').send_keys(JOB_APP['phone'])

        # Upload Resume
        resume_upload = driver.find_element_by_name('resume')
        resume_upload.send_keys(os.path.join(os.getcwd(), JOB_APP['resume']))
        print("Application submitted on Lever.")
    except Exception as e:
        print(f"Failed to apply on Lever: {e}")
