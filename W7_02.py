import sqlite3
import requests

print('START')
#Creating the database
conn = sqlite3.connect('US_DATA.sqlite')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS UsPoverty 
(id INTEGER UNIQUE, year INTEGER, state TEXT, percentage REAL)''')

#Function to convert the GeoId into a real state location that humans can understand
def Geo2Loc(GeoId):
    UrlGeoLocAPIBase="https://api.datausa.io/attrs/geo/"
    UrlGeoLocAPI=UrlGeoLocAPIBase+GeoId+'/'
    jsonGeoLocAPI = requests.get(UrlGeoLocAPI).json()
    DataGeoLocAPI = [dict(zip(jsonGeoLocAPI["headers"], d)) for d in jsonGeoLocAPI["data"]]
    return DataGeoLocAPI[0]['name_long']

url = "https://api.datausa.io/api?show=geo&year=all&sumlevel=state&required=income_below_poverty,pop_poverty_status,income_below_poverty,income_below_poverty_moe,pop_poverty_status,pop_poverty_status_moe&sort=desc&order=income_below_poverty"
json = requests.get(url).json()
data = [dict(zip(json["headers"], d)) for d in json["data"]]

COUNT = 0
for item in data:
    COUNT = COUNT+1
    YEAR = item['year']
    STATE = Geo2Loc(item['geo'])
    PERCENTAGE = 100*item['income_below_poverty']/item['pop_poverty_status']
    cur.execute('''INSERT OR IGNORE INTO UsPoverty (id, year, state, percentage)
                VALUES ( ?, ?, ?, ?)''', (COUNT, YEAR, STATE, PERCENTAGE))

conn.commit()
cur.close()
print('END')