import unittest
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        # self.display = Display(visible=0, size=(800, 600))
        # self.display.start()
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get('http://www.baidu.com')
        self.assertIn('Python', driver.title)
        elem = driver.find_element_by_id('kw')
        elem.send_keys('python')
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
        while True:
            pass

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()