# 页面中的跟浏览器驱动有关的公共操作抽取出来
# 封装在一个单独的类中,作为其他页面对象的基类
from utils import DriverUtil


# 对象库层基类
class BasePage:
    # 获取浏览器驱动对象
    def __init__(self):
        self.driver = DriverUtil.get_driver()

    # 定位页面元素
    # 参数 -- 定位信息
    # 返回 -- 元素对象
    def find_element(self, location):
        return self.driver.find_element(location[0], location[1])


# 操作层基类
class BaseHandle:
    # 元素输入文本
    # 参数 -- 元素对象,输入内容
    def input_text(self, element, text):
        element.clear()
        element.send_keys(text)
