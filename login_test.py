# 로그인

import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
from driver_setup import get_stealth_driver


chromedriver_autoinstaller.install()
driver = get_stealth_driver()

def test_login_success(driver):
    driver.get('https://www.coupang.com/')

    try:
        login_click = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, '로그인'))
        )
        login_click.click()
        print('로그인 페이지 이동')

        login_email = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'login-email-input'))
        )
        login_email.send_keys('test@gmail.com')
        print('이메일 입력')

        login_password = driver.find_element(By.ID, 'login-password-input')
        login_password.send_keys('Test12!34')
        print('비밀번호 입력')

        login_checkbox = driver.find_element(By.CSS_SELECTOR, '._loginSubmitButton')
        login_checkbox.click()
        print('로그인 버튼 클릭 완료')

        main_page = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, '로그아웃'))
        )
        assert main_page.is_displayed()
        print('테스트 성공 : 로그인 후 메인 페이지로 정상 이동했습니다.')

    except Exception as e:
        print(f'오류발생 : {e}')


if __name__ == '__main__':
    test_login_success(driver)
    input()