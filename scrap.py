from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time




class scrapper:

    def __init__(self):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')  
        self.driver = webdriver.Chrome('./chromedriver.exe', chrome_options=options)
        self.dji = {}
        self.hsi = {}
        self.gold = {}
        

    def get_dji(self):
        try:
            self.driver.get('https://www.tradingview.com/markets/indices/quotes-major/')
            dji_index = self.driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div/div/div[2]/div[2]/div[4]/table/tbody/tr[3]/td[2]/span')
            dji_change = self.driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div/div/div[2]/div[2]/div[4]/table/tbody/tr[3]/td[4]')
            dji_change_percent = self.driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div/div/div[2]/div[2]/div[4]/table/tbody/tr[3]/td[3]')
            self.dji = {'dji' : dji_index.text, 'dji_change' : dji_change.text, 'dji_percent' : dji_change_percent.text}
        except:
            print("dji is not successfully scrapped")

    def get_hsi(self):
        try:
            self.driver.get('https://www.tradingview.com/markets/indices/quotes-major/')
            hsi_index = self.driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div/div/div[2]/div[2]/div[4]/table/tbody/tr[13]/td[2]/span')
            hsi_change = self.driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div/div/div[2]/div[2]/div[4]/table/tbody/tr[13]/td[4]')
            hsi_change_percent = self.driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div/div/div[2]/div[2]/div[4]/table/tbody/tr[13]/td[3]')
            self.hsi = {'hsi' : hsi_index.text, 'hsi_change' : hsi_change.text, 'hsi_percent' : hsi_change_percent.text}     
        except:
            print("hsi is not successfully scrapped")   

    def get_gold(self):
            try:
                self.driver.get('https://www.tradingview.com/markets/futures/quotes-metals/')
                time.sleep(0.1)
                gold_index = self.driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div/div/div[2]/div[2]/div[4]/table/tbody/tr[1]/td[2]/span')
                gold_change = self.driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div/div/div[2]/div[2]/div[4]/table/tbody/tr[1]/td[4]')
                gold_change_percent = self.driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div/div/div[2]/div[2]/div[4]/table/tbody/tr[1]/td[3]')
                self.gold = {'gold' : gold_index.text, 'gold_change' : gold_change.text, 'gold_percent' : gold_change_percent.text}
            except:
                print("gold is not successfully scrapped") 

    def close(self):
        self.driver.close()


