# World alcohol consumption analysis with Python

The project in Python for analyzing World bank data about alcohol consumption in different countries in 1980-2016. 

Firstly, the project gives you an overview of the data in general (changes through all years). 

Secondly, you can choose any two years in range 1980-2016, which you would like to compare with each other, see visualization of alcohol consumption in these periods in comparison next to each other and run hypothesis statistical tests to prove if these was a significant change in alcohol consumption between these two years or not.

Before running the project, you have to install the necessary software typing this command in your Terminal/command line:

**python3.6 -m pip install -r requirements.txt --upgrade**

At the beginning I recommend you to run the script with the overview of the data - **overview.py** (alternatively, you can open the confuguration file **config.py**, choose any two years which you would like to compare and run **main.py**.

You can do it with this command in your Terminal (you need to be at the directory of the project at this moment):

python3.6 overview.py

**What happens when you run overview.py:**

1. It shows the descriptive statistics of the data - mean, median, standard deviation etc.

2. It visualizes changes in general world alcohol consumption through years (calculating mean of alcohol consumption value for each year):

![alt text](https://github.com/YaKsenia/world_alcohol_consumption_analysis_python/blob/master/visualizations/overview_alcohol_consumption_all_years.png)

3. It visualizes the number of countries presented in the data for each year (so we can see how many missing data are there in some years, sometimes it can be twice less than in others):

![alt text](https://github.com/YaKsenia/world_alcohol_consumption_analysis_python/blob/master/visualizations/number_of_countries_per_year.png)
