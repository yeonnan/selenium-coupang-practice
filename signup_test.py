# 회원가입

import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
from driver_setup import get_stealth_driver


chromedriver_autoinstaller.install()
driver = get_stealth_driver()


def test_signup_success(driver):
    driver.get('https://www.coupang.com/')
    
    signup_click = driver.find_element(By.LINK_TEXT, '회원가입')
    signup_click.click()
    print('회원가입 페이지 이동')

    signup_email = driver.find_element(By.ID, 'join-email-input')
    signup_email.send_keys('test@gmail.com')
    print('이메일 작성')

    signup_password = driver.find_element(By.ID, 'join-password-input')
    signup_password.send_keys('Test12!34')
    print('비밀번호 작성')

    signup_password_confirm = driver.find_element(By.ID, 'join-password-again-input')
    signup_password_confirm.send_keys('Test12!34')
    print('비밀번호 확인 작성')

    signup_name = driver.find_element(By.ID, 'join-name-input')
    signup_name.send_keys('안다연')
    print('이름 작성')

    signup_phone = driver.find_element(By.ID, 'join-phone-input')
    signup_phone.send_keys('010-1234-5678')
    print('전화번호 작성')

    require_checkbox = driver.find_elements(By.CSS_SELECTOR, '.c-checkbox-item')

    for checkbox in require_checkbox:
        if '[필수]' in checkbox.text:
            checkbox.find_element(By.TAG_NAME, 'label').click()
            time.sleep(0.5)
    print('필수 체크박스 체크')

    submit_button = driver.find_element(By.CSS_SELECTOR, '.join__button.join__button--blue-large-block._joinTrigger')
    submit_button.click()
    time.sleep(0.5)
    print('버튼 클릭')


# 이미 가입된 이메일
def test_signup_duplicate_email(driver):
    driver.get('https://www.coupang.com/')

    try:
        duplicate_signup_click = driver.find_element(By.LINK_TEXT, '회원가입')
        duplicate_signup_click.click()
        print('회원가입 페이지 이동')

        duplicate_email = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID,'join-email-input'))
        )
        duplicate_email.send_keys('pjcu011@gmail.com')
        print('중복된 이메일 작성')
        time.sleep(2)

        duplicate_email.send_keys(Keys.TAB)
        print('TAB으로 비밀번호 칸 이동')

    except Exception as e:
        print(f'오류발생 : {e}')


# 유요하지 않은 이메일
def test_signup_invalid_email(driver):
    driver.get('https://www.coupang.com/')

    try:
        invalid_signup_click = driver.find_element(By.LINK_TEXT, '회원가입')
        invalid_signup_click.click()
        print('회원가입 페이지 이동')
        time.sleep(0.5)

        invalid_email = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID,'join-email-input'))
        )
        invalid_email.send_keys('pjcu011@g@ail.com')
        print('유요하지 않은 이메일 작성')
        time.sleep(2)

        invalid_email.send_keys(Keys.TAB)
        print('TAB으로 비밀번호 칸 이동')

    except Exception as e:
        print(f'오류발생 : {e}')


# 유효하지 않은 비밀번호
def test_signup_invalid_password(driver):
    pass


# signup_test 파일을 직접 실행할 때만 테스트
if __name__ == '__main__':
    # test_signup_success(driver)
    # test_signup_duplicate_email(driver)
    test_signup_invalid_email(driver)
    input()