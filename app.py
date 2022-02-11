from scrap import scrapper
from flask import Flask,render_template
import time
import jyserver.Flask as js

app=Flask(__name__)

@js.use(app)
class App():

    @js.task
    def main(self):
        a = scrapper()
        state = ['dji','hsi','gold']
        while True:
            try:
                for idx in state:
                    if idx == 'dji':
                        a.get_dji()
                        self.js.dom.index_name.innerHTML = "Dow Jones Industrial Average"
                        if("−" in a.dji["dji_change"]):
                            self.js.dom.index_percent.style.color = "red"
                            self.js.dom.index_change.style.color = "red"
                            a.dji["dji_change"] = "&darr;" + a.dji["dji_change"]
                        else:
                            self.js.dom.index_percent.style.color = "green"
                            self.js.dom.index_change.style.color = "green" 
                            a.dji["dji_change"] = "&uarr;" + a.dji["dji_change"]
                        self.js.dom.index.innerHTML = a.dji["dji"]
                        self.js.dom.index_change.innerHTML = a.dji["dji_change"]
                        self.js.dom.index_percent.innerHTML = a.dji["dji_percent"]
                        a.dji={}
                    if idx == 'hsi':
                        a.get_hsi()
                        self.js.dom.index_name.innerHTML = "Hang Seng Index"
                        if("−" in a.hsi["hsi_change"]):
                            self.js.dom.index_percent.style.color = "red"
                            self.js.dom.index_change.style.color = "red"
                            a.hsi["hsi_change"] = "&darr;" + a.hsi["hsi_change"]
                        else:
                            self.js.dom.index_percent.style.color = "green"
                            self.js.dom.index_change.style.color = "green" 
                            a.hsi["hsi_change"] = "&uarr;" + a.hsi["hsi_change"]
                        self.js.dom.index.innerHTML = a.hsi["hsi"]
                        self.js.dom.index_change.innerHTML = a.hsi["hsi_change"]
                        self.js.dom.index_percent.innerHTML = a.hsi["hsi_percent"]
                        a.hsi={}
                    if idx == 'gold':
                        a.get_gold()
                        self.js.dom.index_name.innerHTML = "Gold Futures"
                        if("−" in a.gold["gold_change"]):
                            self.js.dom.index_percent.style.color = "red"
                            self.js.dom.index_change.style.color = "red"
                            a.gold["gold_change"] = "&darr;" + a.gold["gold_change"]
                        else:
                            self.js.dom.index_percent.style.color = "green"
                            self.js.dom.index_change.style.color = "green" 
                            a.gold["gold_change"] = "&uarr;" + a.gold["gold_change"]
                        self.js.dom.index.innerHTML = a.gold["gold"]
                        self.js.dom.index_change.innerHTML = a.gold["gold_change"]
                        self.js.dom.index_percent.innerHTML = a.gold["gold_percent"]
                        a.gold={}
                    time.sleep(10)
            except:
                print("something went wrong")




@app.route('/')
def hello():
    App.main()
    return App.render(render_template('index.html'))
