from selenium import webdriver
browser = webdriver.Firefox()

# 伊迪丝听说在线待办事项应用
# 她去看了首页
browser.get('http://localhost:8000')

# 她注意到 "To-do" 这个词
assert 'To-do' in browser.title

# 她输入一个待办事项

# 她在文本框输入“Buy peacock feathers"

# 按回车后更新页面
# 待办事项表格显示了"1: Buy peacock feathers"

# 页面又出现一个文本框，可以继续输入其它事项
# 她继续输入"Use the feathers to make a fly"

# 页面再次更新，显示两个待办事项

# 网站为她生成器唯一的URL

browser.quit()

