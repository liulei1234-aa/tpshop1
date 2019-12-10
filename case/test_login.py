# 使用 unittest 管理测试用例
import json
import time
import unittest
from parameterized import parameterized

# 数据驱动  --  读取json数据,传入parameterized
from page.login_page import LoginProxy
from utils import DriverUtil, get_tips_msg


def read_data():
    pass


# 1.创建测试类
class TestLogin(unittest.TestCase):
    # 4.fixture -- class
    @classmethod
    def setUpClass(cls):
        # 打开浏览器
        # 获取驱动对象的工具类 -- 获取浏览器驱动
        cls.driver = DriverUtil.get_driver()
        # 获取业务层对象
        cls.login_proxy = LoginProxy()

    @classmethod
    def tearDownClass(cls):
        # 关闭浏览器
        # 获取驱动对象的工具类 -- 退出浏览器驱动
        DriverUtil.quit_driver()

    # 4.fixture -- method
    def setUp(self):
        # 打开页面 -- 驱动调用get方法打开页面
        self.driver.get("http://localhost")
        # 点击首页的登陆链接
        self.driver.find_element_by_link_text("登录").click()

    def tearDown(self):
        # 等待查看结果
        time.sleep(2)

    # 2.创建测试方法
    # 用户名不存在用例

    def test_login01_username_not_exist(self):
        # 业务操作 -- 元素定位和元素操作
        # 输入 用户名 密码  验证码
        # 业务层 login -- 有业务层的对象
        self.login_proxy.login("13112345677", "123456", "8888")

        # 登陆提示信息
        msg = get_tips_msg()
        print(msg)
        self.assertIn("账号不存在", msg)

    # 密码错误用例
    def test_login02_password_error(self):
        # 输入 用户名 密码  验证码
        # 业务层 login
        self.login_proxy.login("13012345678", "654321", "8888")

        # 登陆提示信息
        msg = get_tips_msg()
        print(msg)
        self.assertIn("密码错误", msg)
