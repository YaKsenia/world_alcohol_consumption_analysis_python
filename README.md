# World alcohol consumption analysis with Python

The project in Python for analyzing World bank data about alcohol consumption in different countries in 1980-2016. 

Firstly, the project gives you an overview of the data in general (changes through all years). 

Secondly, you can choose any two years in range 1960-2016, which you would like to compare with each other, see visualization of alcohol consumption in these periods in comparison next to each other and run hypothesis statistical tests to prove if these was a significant change in alcohol consumption between these two years or not.

Before running the project, you have to install the necessary software typing this command in your Terminal/command line:

**python3.6 -m pip install -r requirements.txt --upgrade**

At the beginning it is better to run the script with the overview of the data - **overview.py** (alternatively, you can run **main.py** right away).

You can do it with this command in your Terminal (you need to be at the directory of the project at this moment):

python3 overview.py

**What happens when you run overview.py:**

1. It shows the descriptive statistics of the data - mean, median, standard deviation, minimum and maximum values of alcohol consumption.

2. It visualizes changes in general world alcohol consumption through years (calculating mean of alcohol consumption value for each year):

![alt text](https://github.com/YaKsenia/world_alcohol_consumption_analysis_python/blob/master/visualizations/overview_alcohol_consumption_all_years.png)

3. The amount of data for each year is not equal and, even though we calculate mean values for every year, it can make the results biased. That's why this script also visualizes the number of countries presented in the data for each year (so we can see how many missing data are there in some years, sometimes it can be twice less than in others):

![alt text](https://github.com/YaKsenia/world_alcohol_consumption_analysis_python/blob/master/visualizations/number_of_countries_per_year.png)


Now, you can choose any pair/pairs of years between which you see a significant change on the graph, and compare them. For this you need to run the script **main.py** with the following command:

**Important! You need to specify in this command the two years which you want to compare. Replace 2015 and 2016 with the years you want to analyze: **
  
  python3 main.py --begin_year 2015 --end_year 2016

  
**What happens when you run main.py?**


1. It calculates number of countries where alcohol consumption raised/ dropped/ didn't change in the chosen two years:

![alt text](https://github.com/YaKsenia/world_alcohol_consumption_analysis_python/blob/master/visualizations/output1.png)


2. It visualizes data for 10 top-coutries in alcohol consumption in comparison for the two years of observation:

![alt text](https://github.com/YaKsenia/world_alcohol_consumption_analysis_python/blob/master/visualizations/countries_leaders_2015-2016.png)


3. It visualizes data per each type of alcohol in comparison between the years of observation (the alcohol value for each type is the sum of the values of all countries):

![alt text](https://github.com/YaKsenia/world_alcohol_consumption_analysis_python/blob/master/visualizations/types_alcohol_compare_2015-2016.png)


4. It created ECDFs (Empirical cumulative distribution function) for each type of alcohol for two years in comparison and plots them on one figure (each ECDF graph plots the alcohol value feature of the data in order from least to greatest and shows the whole feature as if is distributed across the data set):

![alt text](https://github.com/YaKsenia/world_alcohol_consumption_analysis_python/blob/master/visualizations/all_ecdfs_2015-2016.png)


5. It creates swarmplots for each type of alcohol for two years in comparison and plots them on one figure. Each dot represents one country. They help us to see the most common amounts of alcohol consumption:

![alt text](https://github.com/YaKsenia/world_alcohol_consumption_analysis_python/blob/master/visualizations/all_swarmplots_2015-2016.png)


6. It generates bootstrap replicates and permutation replicates based on the means of the data and conducts hypothesis tests with them. Generating replicates helps to avoid getting results by chance, to generalize data, and to make sure that the change is statistically significant.

- The hypothesis is: World alcohol consumption in the second year raised/dropped significatly comparing to the first
- Null hypothesis: There was no significant change in world alcohol consumption



At the end the script generates a table with descriptive statistics for each year and hypothesis test results for each type of alcohol: at the last column you can see if there was no significant change (no), positive significant change (raise) or negative significant change (drop):



![alt text](https://github.com/YaKsenia/world_alcohol_consumption_analysis_python/blob/master/visualizations/output2.png)




You can also see the example of a resulting csv-file in the folder **results** of this Git repository. When you run the project locally, the file with your results will be saved in the main project folder.
