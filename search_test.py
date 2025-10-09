# 검색

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
from driver_setup import get_stealth_driver


chromedriver_autoinstaller.install()
driver = get_stealth_driver()

'''
봇 탐지 시스템으로 인해 실행 불가
'''

# 검색
def test_search_success(driver):
    driver.get('https://www.coupang.com/')
    try:
        search_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'q'))
        )
        search_input.send_keys('아이패드' + Keys.RETURN)
        print('유효한 검색어 입력 및 검색 실행')
            
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#productList'))
        )
        print('테스트 성공 : 검색 결과 페이지로 정상 이동했습니다.')

    except Exception as e:
        print(f'오류발생 : {e}')

# 유효하지 않은 키워드
def test_search_no_result(driver):
    # 메인 검색 기능이 봇 탐지로 실행 불가 상태이므로 해당 기능에 종속된 하위 테스트 케이스 역시 진행 불가
    pass


# 대소문자 동일
def test_search_edge(driver):
    # 메인 검색 기능이 봇 탐지로 실행 불가 상태이므로 해당 기능에 종속된 하위 테스트 케이스 역시 진행 불가
    pass


if __name__ == '__main__':
    # test_search_success(driver)       # 봇 탐지로 현재 실행 불가
    input()