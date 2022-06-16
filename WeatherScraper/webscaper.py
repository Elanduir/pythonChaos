import requests
from bs4 import BeautifulSoup
import time
import os
clear = lambda: os.system('clear')

URL = "https://www.wetterstation-wohlen.ch"
temp = ""
hum = ""

while(True):
    page = requests.get(URL)
    
    soup = BeautifulSoup(page.content, "html.parser")
    result = soup.find_all("td", class_="akt_daten_wert farbe_tab_akt")
    cT = temp
    cHum = hum
    temp = result[1].text
    hum = result[2].text
    pre = result[3].text
    if cT != temp or cHum != hum:
        clear()
        print("Temperature: " + temp + "\nHumidity:    " + hum + "\nPressure:    " +pre)
    time.sleep(30)

