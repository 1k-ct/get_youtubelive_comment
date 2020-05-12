import time

import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import pyautogui
pyautogui.FAILSAFE = True # Falseで無効


class Coeuter():
    
    def __init__(self):
        self.driver = webdriver.Chrome("./driver/chromedriver.exe")
    
    def __aoumovie_p(self, channel_url):
        
        self.driver.get(channel_url)
        self.driver.maximize_window()
        self.driver.find_element_by_xpath('//*[@id="tabsContent"]/paper-tab[2]/div').click()

    def __scl_movies(self,x):
        for x in range(1,x,50):
            self.driver.execute_script("window.scrollTo(0, "+str(x)+");")#ここスクロールの場所！！！

    def __bs_soup(self):
        html = self.driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        res_url = soup.find_all(attrs={"class": "style-scope ytd-grid-renderer", "id": "items"})
        try:
            self.a = [tag.get('href') for tag in soup('a')]
        except:
            print('error')
        return self.a

    def __watch_calc(self):
        a_href_list = []
        for ia_href in self.a:
            if ia_href == None:
                pass
            elif "watch" in ia_href:
                a_href_list.append(ia_href)
        del a_href_list[1:len(a_href_list):2]
        
        return a_href_list

    def mninj(self, channel_url, x):

        self.__aoumovie_p(channel_url)
        time.sleep(5)
        self.__scl_movies(x)
        self.__bs_soup()

        self.driver.quit()
        
        return self.__watch_calc()
