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


Now, you can choose any pair/pairs of years between which you see a significant change on the graph, and compare them. For this you need to:

- Open **config.py** file and replace the starting and ending year which you see there with the ones you are interested in.

- Run the script **main.py** with the following command:
  
  python3.6 main.py
  
  
**What happens when you run main.py?**

1. It calculates number of countries where alcohol consumption raised/ dropped/ didn't change in the chosen two years:

![alt text](https://github.com/YaKsenia/world_alcohol_consumption_analysis_python/blob/master/visualizations/output1.png)

2. It visualizes data for 10 top-coutries in alcohol consumption in comparison for the two years of observation:

![alt text](https://github.com/YaKsenia/world_alcohol_consumption_analysis_python/blob/master/visualizations/countries_leaders_2015-2016.png)

3. It visualizes data per each type of alcohol in comparison between the years of observation:

![alt text](https://github.com/YaKsenia/world_alcohol_consumption_analysis_python/blob/master/visualizations/types_alcohol_compare_2015-2016.png)
