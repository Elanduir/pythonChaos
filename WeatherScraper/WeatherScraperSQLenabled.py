#!/usr/bin/env python3
import requests
import mysql.connector
from datetime import datetime
from heat_index import calculate
from bs4 import BeautifulSoup
import time
import os
import random

clear = lambda: os.system('clear')

URL_wohlen = "https://www.wetterstation-wohlen.ch"
URL_lenzburg = "http://www.wetterstation-niederlenz.ch/custom.html"

config = {
    "user": "root",
    "password": "wasser1",
    "host": "192.168.10.73",
    "port": "3306",
    "database": "db_weather"
}

db = mysql.connector.connect(**config)
dbcursor = db.cursor()
sqlW = "INSERT INTO 5610_wohlen_cache (date_created, temperature, humidity, pressure, heatIndex) VALUES (%s, %s, %s, %s, %s)"
sqlL = "INSERT INTO 5600_lenzburg_cache (date_created, temperature, humidity, pressure, heatIndex) VALUES (%s, %s, %s, %s, %s)"

while(True):
    fDate = datetime.now().strftime('%Y-%m-%d %H:%M')
    
    pageW = requests.get(URL_wohlen)
    pageL = requests.get(URL_lenzburg)

    soupW = BeautifulSoup(pageW.content, "html.parser")
    soupL = BeautifulSoup(pageL.content, "html.parser")

    resultW = soupW.find_all("td", class_="akt_daten_wert farbe_tab_akt")
    resultL = soupL.find_all("span", class_="Stil3")
    
    rHW = soupW.find_all("td", class_="akt_daten_wert farbe_tab_stat")

    tempW = resultW[1].text[0:4]
    humW = resultW[2].text[0:2]
    preW = resultW[3].text[0:6]
    hdexW = rHW[1].text[0:4]

    tempL = resultL[0].text.strip()[0:4]
    humL = resultL[4].text.strip()[0:2]
    preL = resultL[12].text.strip().splitlines()[0][0:6]
    hdexL = round(calculate.from_celsius(tempL, humL), 1)

    valW = (fDate, float(tempW), float(humW), float(preW), float(hdexW))
    valL = (fDate, float(tempL), float(humL), float(preL), hdexL)

    
    dbcursor.execute(sqlW, valW)
    dbcursor.execute(sqlL, valL)
    db.commit()
    print("Wrote data to DB")
    time.sleep(600)

