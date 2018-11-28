Step 0:
To understand the dataset visit the website:
https://datausa.io/

More importantly take a look:
https://datausa.io/map/?level=state&key=owner_occupied_housing_units

https://datausa.io/map/?level=state&key=income_below_poverty:pop_poverty_status,income_below_poverty,income_below_poverty_moe,pop_poverty_status,pop_poverty_status_moe&translate=3745.461808599117,5922.01107093552&scale=37729.36747360798

TO VIEW THE API URL CLICK ON VIEW DATA

Step 1:
Run in terminal.
$pip install requests

Step 2:
To understand the API visit the website:
https://github.com/DataUSA/datausa-api/wiki/Getting-Started#python

Step 3:
Run in terminal.
$python3 W7_01.py
Takes about a minute and creates US_DATA.sqlite with the table UsOwner.

Step 4:
Run in terminal.
$python3 W7_02.py
Takes about a minute and creates in US_DATA.sqlite the table UsPoverty.

Step 5:
Run in terminal.
$python3 W7_03.py
Takes a second and creates in US_DATA_CLEAN.sqlite the tables State, Poverty and Owner.
This step is just to have nicer tables.

Step 6:
To understand the visualization visit the website:
https://developers.google.com/chart/interactive/docs/gallery/scatterchart

Step 7:
Run in terminal.
$python3 W7_04.py
Takes a second and creates the file W7_05.js used in the visualization.

Step 8:
Run in terminal.
$open W7_06.htm
This opens a browser with a scatter plot. 
On the x-axis the Poverty rate and on the y-axis the Ownership rate. 

Step 9:
The plot shows no relationship between Poverty and Ownership. 
This is unexpected and counterintuitive!
I expected states with higher Poverty rates to have a lower Ownership rates.