# 장바구니

import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
from driver_setup import get_stealth_driver


chromedriver_autoinstaller.install()
driver = get_stealth_driver()


# 로그인 상태
def perform_login(driver, user_id, user_password):
    driver.get('https://login.coupang.com/login/login.pang')
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'login-email-input'))
    ).send_keys(user_id)

    driver.find_element(By.ID, 'login-password-input').send_keys(user_password)
    driver.find_element(By.CSS_SELECTOR, '._loginSubmitButton').click()
    print('로그인 완료 후 메인페이지로 이동')

'''
봇 탐지 시스템으로 인해 실행 불가
'''

# 장바구니 담기
def test_add_item_cart(driver):
    try:
        perform_login(driver, 'test@gmail.com', 'Test12!34')
        time.sleep(2)

        # TC의 검색 단계는 봇 탐지 이슈로 인해 상품 페이지 url로 직접 이동하여 수행
        product_url = 'https://www.coupang.com/vp/products/8090487679'
        driver.get(product_url)
        print('상품 페이지로 이동')

        add_cart = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.prod-cart-btn'))
        )
        add_cart.click()
        print('장바구니 담기 버튼 클릭')

        success_modal = WebDriverWait(driver, 10).until(
            EC.visibility_of_any_elements_located((By.CSS_SELECTOR, '.prod-order-notifier-content'))
        )
        assert success_modal.is_displayed()
        print('테스트 성공 : "상품이 장바구니에 담겼습니다." 팝업 확인')

    except Exception as e:
        print(f'오류발생 : {e}')


# 장바구니 바로가기 선택
def test_navigate_cart_page(driver):
    pass


# 장바구니에서 상품 수량 증가
def test_increase_item_quantity_cart(driver):
    pass


# 수량 제한
def test_limit_item_cart(driver):
    pass



if __name__ == '__main__':
    test_add_item_cart(driver)
    input()