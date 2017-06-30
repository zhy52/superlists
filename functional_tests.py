from selenium import webdriver
import unittest

class NewVIstorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(10)
        
    def tearDown(self):
        self.browser.quit()
        
    def test_can_start_a_list_and_retrieve_it_later(self):
        # 伊迪丝听说在线待办事项应用
        # 她去看了应用首页
        self.browser.get('http://localhost:8000')

        # 她注意到网页标题和头部都有 "To-do" 这个词
        self.assertIn('To-do', self.browser.title) 
        self.fail('Finish the test!') 

        # 应用邀请她输入一个待办事项

        # 她在文本框输入“Buy peacock feathers"
        # 她的爱好是使用假蝇做饵钓鱼

        # 她按回车后，页面更新了
        # 待办事项表格显示了"1: Buy peacock feathers"

        # 页面又出现一个文本框，可以继续输入其它事项
        # 她继续输入"Use the feathers to make a fly"

        # 页面再次更新，她的清单中显示两个待办事项

        # 伊迪丝想知道这个网站是否会记住她的清单
        # 她看到网站为她生成唯一的URL
        # 而且页面中有一些文字说明
        
        # 她访问那个URL，发现她的待办列表还在
        
        # 她很满意，走了
        
if __name__ == '__main__':
    unittest.main(warnings="ignore")


