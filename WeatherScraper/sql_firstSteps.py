import mysql.connector
from datetime import datetime, timedelta
now = datetime.now() - timedelta(days=1)
formated_date = now.strftime('%Y-%m-%d %H:%M:%S')

config = {
    "user": "root",
    "password": "wasser1",
    "host": "172.17.0.2",
    "port": "3306",
    "database": "db_weather"
}

connection = mysql.connector.connect(**config)

mycursor = connection.cursor()

sql = "INSERT INTO 5610_wohlen_cache (date_created, temperature, humidity, pressure) VALUES (%s, %s, %s, %s)"
val = (formated_date, 10, 10, 10)

mycursor.execute(sql, val)

connection.commit()

connection.close()
