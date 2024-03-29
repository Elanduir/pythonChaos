import requests
import cursor
import shutil
from bs4 import BeautifulSoup
import time
import os
clear = lambda: os.system('clear')

URL_wohlen = "https://www.wetterstation-wohlen.ch"
URL_lenzburg = "http://www.wetterstation-niederlenz.ch/custom.html"
tempW = ""
humW = ""
tempL = ""
humL = ""

cursor.hide()

while(True):
    columns = shutil.get_terminal_size().columns
    rows = int(shutil.get_terminal_size().lines / 2 - 1)
    pageW = requests.get(URL_wohlen)
    pageL = requests.get(URL_lenzburg)

    soupW = BeautifulSoup(pageW.content, "html.parser")
    soupL = BeautifulSoup(pageL.content, "html.parser")

    resultW = soupW.find_all("td", class_="akt_daten_wert farbe_tab_akt")
    resultL = soupL.find_all("span", class_="Stil3")

    cTW = tempW
    cHumW = humW
    cTL = tempL
    cHumL = humL

    tempW = resultW[1].text
    humW = resultW[2].text
    preW = resultW[3].text

    tempL = resultL[0].text[0:-10]
    humL = resultL[4].text
    preL = resultL[12].text

    if cTW != tempW or cHumW != humW:
        clear()
        for x in range(0,rows):
            print("")
        print(("Temperature: " + tempW).center(columns))
        print(("Humidity: " + humW).center(columns))
        print(("Pressure: " +preW).center(columns))
        #print("Temperature: " + tempL + "\nHumidity:    " + humL + "\nPressure:    " +preL)
    time.sleep(30)

