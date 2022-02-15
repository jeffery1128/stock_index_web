from concurrent.futures import thread
from scrap import scrapper
from flask import Flask,render_template
import time
import jyserver.Flask as js
import threading

app=Flask(__name__)

@js.use(app)
class App():

    def __init__(self):
        self.scrapper = scrapper()
        self.wait_interval = 3
        self.update_time_interval =20

    def scrapping(self):
            dji_result_flag = self.scrapper.get_dji()
            time.sleep(self.wait_interval)
            hsi_result_flag = self.scrapper.get_hsi()
            time.sleep(self.wait_interval)
            gold_result_flag = self.scrapper.get_gold()
            time.sleep(self.wait_interval)

    def update_DOM(self):
            state = ['dji','hsi','gold']
            for idx in state:
                if idx=="dji":
                    self.js.dom.index_name.innerHTML = "Dow Jones Industrial Average"
                    if("−" in self.scrapper.dji["dji_change"]):
                        self.js.dom.index_percent.style.color = "red"
                        self.js.dom.index_change.style.color = "red"
                        if("&darr;" not in self.scrapper.dji["dji_change"]):
                            self.scrapper.dji["dji_change"] = "&darr;" + self.scrapper.dji["dji_change"]
                    else:
                        self.js.dom.index_percent.style.color = "green"
                        self.js.dom.index_change.style.color = "green"
                        if("&uarr;" not in self.scrapper.dji["dji_change"]):
                            self.scrapper.dji["dji_change"] = "&uarr;" + self.scrapper.dji["dji_change"]
                    self.js.dom.index.innerHTML = self.scrapper.dji["dji"]
                    self.js.dom.index_change.innerHTML = self.scrapper.dji["dji_change"]
                    self.js.dom.index_percent.innerHTML = self.scrapper.dji["dji_percent"]
                if idx=="hsi":
                    self.js.dom.index_name.innerHTML = "Hang Seng Index"
                    if("−" in self.scrapper.hsi["hsi_change"]):
                        self.js.dom.index_percent.style.color = "red"
                        self.js.dom.index_change.style.color = "red"
                        if("&darr;" not in self.scrapper.hsi["hsi_change"]):
                            self.scrapper.hsi["hsi_change"] = "&darr;" + self.scrapper.hsi["hsi_change"]
                    else:
                        self.js.dom.index_percent.style.color = "green"
                        self.js.dom.index_change.style.color = "green"
                        if("&uarr;" not in self.scrapper.hsi["hsi_change"]):
                            self.scrapper.hsi["hsi_change"] = "&uarr;" + self.scrapper.hsi["hsi_change"]
                    self.js.dom.index.innerHTML = self.scrapper.hsi["hsi"]
                    self.js.dom.index_change.innerHTML = self.scrapper.hsi["hsi_change"]
                    self.js.dom.index_percent.innerHTML = self.scrapper.hsi["hsi_percent"]
                if idx=="gold":
                    self.js.dom.index_name.innerHTML = "Gold Futures"
                    if("−" in self.scrapper.gold["gold_change"]):
                        self.js.dom.index_percent.style.color = "red"
                        self.js.dom.index_change.style.color = "red"
                        if("&darr;" not in self.scrapper.gold["gold_change"]):
                            self.scrapper.gold["gold_change"] = "&darr;" + self.scrapper.gold["gold_change"]
                    else:
                        self.js.dom.index_percent.style.color = "green"
                        self.js.dom.index_change.style.color = "green"
                        if("&uarr;" not in self.scrapper.gold["gold_change"]):
                            self.scrapper.gold["gold_change"] = "&uarr;" + self.scrapper.gold["gold_change"]
                    self.js.dom.index.innerHTML = self.scrapper.gold["gold"]
                    self.js.dom.index_change.innerHTML = self.scrapper.gold["gold_change"]
                    self.js.dom.index_percent.innerHTML = self.scrapper.gold["gold_percent"]
                time.sleep(self.update_time_interval)


    @js.task
    def main(self):
        while True:
            self.scrapping()
            self.update_DOM()

        

                




@app.route('/')
def hello():
    App.main()
    return App.render(render_template('index.html'))
