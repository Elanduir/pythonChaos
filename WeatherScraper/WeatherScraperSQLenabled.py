#!/usr/bin/env python3
import requests
import mysql.connector
from datetime import datetime
from bs4 import BeautifulSoup
import time
import os

clear = lambda: os.system('clear')

URL_wohlen = "https://www.wetterstation-wohlen.ch"
URL_lenzburg = "http://www.wetterstation-niederlenz.ch/custom.html"

config = {
    "user": "root",
    "password": "wasser1",
    "host": "192.168.10.74",
    "port": "3306",
    "database": "db_weather"
}

db = mysql.connector.connect(**config)
dbcursor = db.cursor()
sqlW = "INSERT INTO 5610_wohlen_cache (date_created, temperature, humidity, pressure) VALUES (%s, %s, %s, %s)"
sqlL = "INSERT INTO 5600_lenzburg_cache (date_created, temperature, humidity, pressure) VALUES (%s, %s, %s, %s)"

while(True):
    fDate = datetime.now().strftime('%Y-%m-%d %H:%M')
    

    pageW = requests.get(
        url=URL_wohlen,
        params={
            'api_key': 'D132W2C3AJ60FCWT0EVEG6Y006YC27XJMFWXY53XDMEO78AZICQ7IZR4TNW05LEQLC07X51ANF9WEI1O',
            'url': 'http://httpbin.org/anything?json',  
        },
    )

    print(pageW)

    pageL = requests.get(URL_lenzburg)

    soupW = BeautifulSoup(pageW.content, "html.parser")
    soupL = BeautifulSoup(pageL.content, "html.parser")

    resultW = soupW.find_all("td", class_="akt_daten_wert farbe_tab_akt")
    resultL = soupL.find_all("span", class_="Stil3")

    tempW = resultW[1].text
    humW = resultW[2].text
    preW = resultW[3].text

    tempL = resultL[0].text.strip()
    humL = resultL[4].text.strip()
    preL = resultL[12].text.strip().splitlines()[0]

    valW = (fDate, float(tempW[0:4]), float(humW[0:2]), float(preW[0:6]))
    valL = (fDate, float(tempL[0:4]), float(humL[0:2]), float(preL[0:6]))
    

    print(valL)

    dbcursor.execute(sqlW, valW)
    dbcursor.execute(sqlL, valL)
    db.commit()
    print("Wrote data to DB")
    time.sleep(60)

