from selenium import webdriver
import time

#导入键盘类
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
#无界面的平台
# driver = webdriver.PhantomJS(executable_path=r'C:\phantomjs-2.1.1-windows\bin\phantomjs.exe')



# ------------------------登陆测试-------------------------------------
class LoginIn_test():
    def __init__(self,url,drivers,kwargs):
        self.url = url
        self.args = kwargs
        self.driver =drivers

    def open_url(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
    def handel(self):
        self.driver.find_element_by_link_text(self.args['login']).click()
        time.sleep(2)
        self.driver.find_element_by_name(self.args['username']).send_keys('maizi_test@139.com')
        time.sleep(2)
        self.driver.find_element_by_id(self.args['pwd']).send_keys('abc123456')
        time.sleep(2)
        self.driver.find_element_by_id(self.args['login_btn']).click()

    def run(self):
        self.open_url()
        time.sleep(4)
        # print('self.args',self.args)
        self.handel()
        time.sleep(4)
        self.quit()
    def quit(self):
        self.driver.quit()
def main():
    first_url = 'http://www.maiziedu.com/'
    Browser = 'Chrome'
    element_dict = {'login': '登录',
                    'username': 'account_l',
                    'pwd': 'id_password_l',
                    'login_btn': 'login_btn'}

    if Browser == 'Firefox':
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        login = LoginIn_test(first_url,driver, element_dict)
        login.run()
    elif Browser == 'Ie':
        driver = webdriver.Ie()
        driver.implicitly_wait(10)
        login = LoginIn_test(first_url, driver,element_dict)
    elif Browser == 'Chrome':
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        login = LoginIn_test( first_url,driver, element_dict)
        login.run()
if __name__ == '__main__':
    main()

