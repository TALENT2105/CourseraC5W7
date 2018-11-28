import sqlite3
import requests

print('START')

#Creating the database
conn = sqlite3.connect('US_DATA.sqlite')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS UsOwner (id INTEGER UNIQUE, year INTEGER, state TEXT, owner REAL)''')

#Function to convert the GeoId into a real state location that humans can understand
def Geo2Loc(GeoId):
    UrlGeoLocAPIBase="https://api.datausa.io/attrs/geo/"
    UrlGeoLocAPI=UrlGeoLocAPIBase+GeoId+'/'
    jsonGeoLocAPI = requests.get(UrlGeoLocAPI).json()
    DataGeoLocAPI = [dict(zip(jsonGeoLocAPI["headers"], d)) for d in jsonGeoLocAPI["data"]]
    return DataGeoLocAPI[0]['name_long']

url2="https://api.datausa.io/api?show=geo&year=all&sumlevel=state&required=owner_occupied_housing_units&sort=desc&order=owner_occupied_housing_units"
json2 = requests.get(url2).json()
data2 = [dict(zip(json2["headers"], d)) for d in json2["data"]]

COUNT = 0
for item in data2:
    COUNT = COUNT+1
    YEAR = item['year']
    STATE = Geo2Loc(item['geo'])
    OWNER = 100*item['owner_occupied_housing_units']
    cur.execute('''INSERT OR IGNORE INTO UsOwner (id, year, state, owner)
                    VALUES ( ?, ?, ?, ?)''', (COUNT, YEAR, STATE, OWNER))

conn.commit()
cur.close()
print('END')