from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


class LoginPage(BasePage):
    def __init__(self):
        # 调用父类init方法
        super().__init__()

        # 初始化页面元素定位依据  --  通过元素管理元素定位信息(定位策略,定位依据)
        # 用户名
        self.username = (By.ID, "username")
        # 密码
        self.pwd = (By.ID, "password")
        # 验证码
        self.verify_code = (By.ID, "verify_code")
        # 登录按钮
        self.login_btn = (By.NAME, "sbtbutton")

    # 元素定位方法 -- 调用父类find_element方法,传入元素定位信息
    # 定位返回用户名对象
    def find_username(self):
        return self.find_element(self.username)

    # 定位返回密码对象
    def find_pwd(self):
        return self.find_element(self.pwd)

    # 定位返回验证码对象
    def find_verify_code(self):
        return self.find_element(self.verify_code)

    # 定位返回登录按钮对象
    def find_login_btn(self):
        return self.find_element(self.login_btn)


class LoginHandle(BaseHandle):
    # 获取到页面元素
    def __init__(self):
        self.login_page = LoginPage()

    # 封装元素操作  调用父类输入文本操作 传入 输入的文本框,和输入的内容
    # 用户名输入操作
    def input_username(self, username):
        self.input_text(self.login_page.find_username(), username)

    # 密码输入操作
    def input_pwd(self, password):
        self.input_text(self.login_page.find_pwd(), password)

    # 验证码输入操作
    def input_verify_code(self, verify_code):
        self.input_text(self.login_page.find_verify_code(), verify_code)

    # 登录按钮点击操作
    def click_login_btn(self):
        self.login_page.find_login_btn().click()


class LoginProxy:

    # 获取页面操作
    def __init__(self):
        self.login_handle = LoginHandle()

    # 组装业务操作
    # 登录业务
    def login(self, username, pwd, verify_code):
        # 输入用户民,密码,验证码,点击登陆
        self.login_handle.input_username(username)
        self.login_handle.input_pwd(pwd)
        self.login_handle.input_verify_code(verify_code)
        self.login_handle.click_login_btn()
