# World alcohol consumption analysis with Python

The project in Python for analyzing World bank data about alcohol consumption in different countries in 1960-2016. It provides a user with tools to compare world alcohol consumption in any two years, use statistical tests to check statistical significance of the observed difference, and also to visualize alcohol consumption data of any specified country.

Firstly, the project gives an overview of the data in general (changes through all years). 

Secondly, you can choose any two years in range 1960-2016, which you would like to compare with each other, see visualization of alcohol consumption in these periods in comparison next to each other and get the results of hypothesis statistical tests which define if there was a significant change in alcohol consumption between these two years or not.

Thirdly, the project generates statistical information and visualization for any country of a user's choice.

Before running the project, you have to install the necessary software typing this command in your Terminal/command line:

**python3 -m pip install -r requirements.txt --upgrade**

At the beginning it is better to run the script with the overview of the data - **overview.py** (alternatively, you can run **main.py** right away).

You can do it with this command in your Terminal (you need to be at the directory of the project at this moment):

python3 overview.py

**What happens when you run overview.py:**

1. It shows the descriptive statistics of the data - mean, median, standard deviation, minimum and maximum values of alcohol consumption.

2. It visualizes changes in general world alcohol consumption through years (calculating mean of alcohol consumption value of all countries for each year):

![alt text](https://github.com/YaKsenia/world_alcohol_consumption_analysis_python/blob/master/visualizations/all_years_overview_alcohol_consumption.png)

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


# Analysis per country of choice

The script **analyze_one_country.py** shows statistical information about the alcohol consumption of any country the user chooses, and visualises data in general, per each type of alcohol and plots ECDF (empirical cumulative distribution function).

Before running this program, you need to choose one country from this list and use its name exactly how it is written there (e. g. you can't use 'Russia', but only 'Russian Federation'):

['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia (Plurinational State of)', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cambodia', 'Cameroon', 'Canada', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo', 'Cook Islands', 'Costa Rica', 'Croatia', 'Cuba', 'Cyprus', 'Czechia', "Côte d'Ivoire", "Democratic People's Republic of Korea", 'Democratic Republic of the Congo', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran (Islamic Republic of)', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Kuwait', 'Kyrgyzstan', "Lao People's Democratic Republic", 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Lithuania', 'Luxembourg', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia (Federated States of)', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norway', 'Oman', 'Pakistan', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Republic of Korea', 'Republic of Moldova', 'Republic of North Macedonia', 'Romania', 'Russian Federation', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent and the Grenadines', 'Samoa', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syrian Arab Republic', 'Tajikistan', 'Thailand', 'Timor-Leste', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom of Great Britain and Northern Ireland', 'United Republic of Tanzania', 'United States of America', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela (Bolivarian Republic of)', 'Viet Nam', 'Yemen', 'Zambia', 'Zimbabwe']

This is the command you need to use for running the program:

**Important! Replace "Russian Federation' with the name of the country you want to analyze, and don't forget to use quotes.**

python3 analyze_one_country.py --country 'Russian Federation'

1. First of all, it will give you some statistical information:

![alt text](https://github.com/YaKsenia/world_alcohol_consumption_analysis_python/blob/master/visualizations/one_country/stats_one_country.png)

2. Then the script visualizes the overview of changes in alcohol consumption in the country:


![alt text](https://github.com/YaKsenia/world_alcohol_consumption_analysis_python/blob/master/visualizations/one_country/overview_alcohol_consumption_Russian_Federation.png)

3. It also visualizes consumption of different types of alcohol through years in this country in comparison:


![alt text](https://github.com/YaKsenia/world_alcohol_consumption_analysis_python/blob/master/visualizations/one_country/types_alcohol_compare_Russian_Federation.png)

4. At the end it plots ECDF of the general alcohol consumption in the country:

![alt text](https://github.com/YaKsenia/world_alcohol_consumption_analysis_python/blob/master/visualizations/one_country/ecdf_Russian_Federation.png)

To be continued... ;)
