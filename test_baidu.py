import sys
from time import  sleep
from os.path import dirname,abspath
sys.path.insert(0,dirname(dirname(abspath(__file__))))
from page.baidu_page import BaiduPage

class Testsearch():
    '''百度搜索'''
    def test_baidu_search_case(self,browser,base_url):
        '''百度搜索pytest'''
        page = BaiduPage(browser)
        page.get(base_url)
        page.search_input = 'pytest'
        page.search_button.click()
        sleep(2)
        assert browser.title == 'pytest_百度搜索'


