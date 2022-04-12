from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pytest
import time
from selenium.webdriver.support.ui import Select

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = None

def test_Senario1(params):

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(8)
    driver.delete_all_cookies()

    driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
    driver.maximize_window()
    # login credentials
    driver.find_element(By.ID, "txtUsername").send_keys(params["username"])
    driver.find_element(By.ID, "txtPassword").send_keys(params['password'])
    driver.find_element(By.ID, "btnLogin").click()

    driver.find_element(By.ID, "menu_recruitment_viewRecruitmentModule").click()
    driver.find_element(By.ID, "btnAdd").click()
    # Entering details (firstname,middlename,lastname,email,phone)
    driver.find_element(By.NAME, "addCandidate[firstName]").send_keys("Radhika")
    driver.find_element(By.NAME, "addCandidate[middleName]").send_keys("Rajiv")
    driver.find_element(By.NAME, "addCandidate[lastName]").send_keys("Dewang")
    driver.find_element(By.ID, "addCandidate_email").send_keys("radhika.dewang12@gmail.com")
    driver.find_element(By.NAME, "addCandidate[contactNo]").send_keys("5028766236")

    ele = driver.find_element(By.ID, "addCandidate_vacancy")
    selectval = Select(ele)
    selectval.select_by_visible_text("Software Engineer")

    '''try:
        openfile = open("Trial.txt","w+")
    except FileNotFoundError:
        print("No such file or directory")
    finally:
        pass

    driver.find_element(By.ID, "addCandidate_resume").send_keys("E:\jinterview.txt")'''

    driver.find_element(By.NAME, "addCandidate[keyWords]").send_keys("QA automation")
    driver.find_element(By.NAME, "addCandidate[comment]").send_keys("QA automation,selenium")

    driver.find_element(By.ID, "addCandidate_appliedDate").send_keys("2022-04-08")
    wait = WebDriverWait(driver, 4)
    driver.find_element(By.NAME, "addCandidate[consentToKeepData]").click()
    #element = wait.until(EC.element_to_be_clickable((By.NAME,"addCandidate[consentToKeepData]")))
    #element.click()
    #wait.until(EC.element_to_be_clickable((By.NAME,"addCandidate[consentToKeepData]"))).click()
    #driver.find_element(By.NAME, "addCandidate[consentToKeepData]").click()
    driver.find_element(By.ID, "btnSave").click()

    wait = WebDriverWait(driver, 4)
    # To check if the element is present in DOM
    result = wait.until(EC.element_located_selection_state_to_be((By.ID, "successBodyEdit"),
                                                                 False))
    time.sleep(2)
    print(result)

    driver.quit()

def test_Senario2(params):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(8)
    driver.delete_all_cookies()

    driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
    driver.maximize_window()
    driver.find_element(By.ID, "txtUsername").send_keys(params["username"])
    driver.find_element(By.ID, "txtPassword").send_keys(params['password'])
    driver.find_element(By.ID, "btnLogin").click()
    driver.find_element(By.ID, "menu_recruitment_viewRecruitmentModule").click()

    ele2 = driver.find_element(By.ID, "candidateSearch_jobTitle")
    selectval2 = Select(ele2)
    selectval2.select_by_visible_text("Software Engineer")

    driver.find_element(By.NAME, "candidateSearch[candidateName]").send_keys("Jennifer Clinton")
    driver.find_element(By.ID, "btnSrch").click()
    resume = driver.find_element(By.XPATH, "//*[@id='resultTable']/tbody/tr[2]/td[7]/a")
    resume.click()