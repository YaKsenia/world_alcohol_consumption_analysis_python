import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('data_world_alcohol_consumption.csv')
#pd.set_option('display.max_rows', df.shape[0]+1)
print('Number of rows and columns of the original data:', df.shape)

#Exploratory data analysis

overview = df.copy()

#create new columns "Year" and 'Value' instead of all the columns with years

overview = overview.melt(id_vars=['Unnamed: 0', 'Country', 'Data Source_x', 'Beverage Types'],
                         var_name="Year",
                         value_name="Value")

#delete the rows with null values
overview = overview.loc[overview.Value.notnull()]

#remove rows where alcohol consumption value is 0
overview = overview[overview['Value'] != 0.0]

#keep the rows with data for all types of alcohol
overview = overview[overview['Beverage Types'] == 'All types']

print('Number of rows and columns of the data after processing:', overview.shape, '\n')
print('Statistics of the "Value" column: ', '\n', overview.Value.describe(), '\n')

#convert year column to integer datatype
overview.Year = overview.Year.astype('int')

#create a new dataframe which groups data by year and calculates the number of items per each year
countries_distribution = overview.groupby(by=['Year']).count().reset_index()

#group the data by year and calculate mean value for each year
overview = overview.groupby(by=['Year']).mean().reset_index()

sns.set_color_codes("pastel")

#visualize changes of alcohol consumption means for every year

_ = plt.plot(overview["Year"], overview["Value"], color='r')

plt.margins(0.02)

# Add axis labels and legend
_ = plt.xlabel('Year')
_ = plt.ylabel('Alcohol consumption value')


#save the graph as png image or show (uncomment the option which you prefer)

#plt.savefig('overview_alcohol_consumption_all_years.png' , dpi=300)
plt.show()
plt.close()


#plot of the number of countries per each year in our data

_ = plt.plot(countries_distribution["Year"], countries_distribution["Country"], color='g')

plt.margins(0.02)

# Add axis labels and legend
_ = plt.xlabel('Year')
_ = plt.ylabel('Number of countries presented')
#plt.savefig('number_of_countries_per_year.png' , dpi=300)
plt.show()
plt.close()
