# the location and name of this file is going to change!
import requests
import time
import re
from pprint import pprint
from bs4 import BeautifulSoup


class Get_Page():
    def __init__(self, payload):
        self.payload = payload
        self.url_s = 'https://gymherderschule.de/iserv/login_check'
        self.url_today = 'https://gymherderschule.de/iserv/infodisplay/file/23/infodisplay/0/SchuelerOnline/subst_001.htm'
        self.url_tomorow = 'https://gymherderschule.de/iserv/infodisplay/file/23/infodisplay/0/SchuelerOnline/subst_002.htm'
        self.headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0'}
        self.title_today = None
        self.massage_today = None
        self.content_today = None
        self.title_tomorow = None
        self.massage_tomorow = None
        self.content_tomorow = None
        self.get_page()

    def update(self):
        self.get_page()


    @staticmethod
    def soup(file):
        return BeautifulSoup(file, "html.parser")


    def formatting(self, source):
        raw_list = self.soup(source).find(class_="mon_list")
        contents = self.soup(str(raw_list)).get_text(separator="|")
        raw_title = self.soup(source).find(class_="mon_title")
        title = self.soup(str(raw_title)).get_text(separator="|")
        raw_massage = self.soup(source).find(class_="info")
        massage = self.soup(str(raw_massage)).get_text(separator="")
        contents = re.split("\n", contents)
        return title, massage, contents


    def get_page(self):
        sess = requests.Session()
        sess.post(self.url_s, data=self.payload, headers=self.headers)
        time.sleep(0.1)
        request_data_today = sess.get(self.url_today, headers=self.headers)
        request_data_tomorow = sess.get(self.url_tomorow, headers=self.headers)
        self.title_today, self.massage_today, self.content_today = self.formatting(request_data_today.content)
        self.title_tomorow, self.massage_tomorow, self.content_tomorow = self.formatting(request_data_tomorow.content)


