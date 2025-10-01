# 로그인

import time
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
from driver_setup import get_stealth_driver


chromedriver_autoinstaller.install()
driver = get_stealth_driver()

def test_login(driver):
    driver.get('https://www.coupang.com/')
    
    login_click = driver.find_element(By.LINK_TEXT, '로그인')
    login_click.click()
    print('로그인 페이지 이동')
    time.sleep(0.8)

    login_email = driver.find_element(By.ID, 'login-email-input')
    login_email.send_keys('test@gmail.com')
    print('이메일 입력')
    time.sleep(0.8)

    login_password = driver.find_element(By.ID, 'login-password-input')
    login_password.send_keys('Test12!34')
    print('비밀번호 입력')
    time.sleep(0.8)

    login_checkbox = driver.find_element(By.CSS_SELECTOR, '._loginSubmitButton')
    login_checkbox.click()
    print('로그인 버튼 클릭 완료')


if __name__ == '__main__':
    test_login(driver)
    input()