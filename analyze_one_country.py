import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statistical_tests import ecdf
from config import filename
import argparse

# Define the parser
parser = argparse.ArgumentParser(description='Define the start and end year')

# Declare an argument (`--algo`), telling that the corresponding value should be stored in the `algo` field, and using a default value if the argument isn't given
parser.add_argument('--country', action="store", dest='data', default="Austria")

# Now, parse the command line arguments and store the values in the `args` variable
parse_years = parser.parse_args()

country = str(parse_years.data)

#read the file

df = pd.read_csv(filename)

#merge all years into one column

df = df.melt(id_vars=['Unnamed: 0', 'Country', 'Data Source_x', 'Beverage Types'],
             var_name="Year",
             value_name="Value")

#Find thw place of the observed country in the world alcohol consumption ranking

ranking = df.copy()
ranking = ranking[ranking['Beverage Types'] == 'All types']
ranking = ranking.groupby('Country').mean().sort_values(by='Value', ascending=False).reset_index()
country_of_research = ranking[ranking['Country'] == country]
print('Place of', country, 'in world alcohol consumption ranking: ', country_of_research.index.tolist())


df = df[df['Country'] == country]

print("Statistics of the alcohol consumption value data of", country, ': ' '\n', df.Value.describe())

#convert year column to integer datatype

df.Year = df.Year.astype('int')

#Overview graph

overview = df.copy()

#keep the rows with data for all types of alcohol
overview = overview[overview['Beverage Types'] == 'All types']

#group the data by year and calculate mean value for each year

overview = overview.groupby(by=['Year']).mean().reset_index()

sns.set_color_codes("pastel")

#visualize changes of alcohol consumption means for every year

_ = plt.plot(overview["Year"], overview["Value"], color='r')

plt.margins(0.02)

# Add axis labels and legend
_ = plt.title('Overview of alcohol consumption in 1960-2016 in ' + country)
_ = plt.xlabel('Year')
_ = plt.ylabel('Alcohol consumption value')


#save the graph as png image or show (uncomment the option which you prefer)

country_processed = country.replace(' ', '_')
plt.savefig('visualizations/one_country/overview_alcohol_consumption_' + country_processed + '.png' , dpi=200)
plt.show()
plt.close()



types_df = df.copy()
#types_df = types_df[types_df['Beverage Types'] != 'All types']

_ = plt.title('Comparison of consumption of different drinks in ' + country)

beer  = types_df[types_df['Beverage Types'] == 'Beer']
wine = types_df[types_df['Beverage Types'] == 'Wine']
spirits = types_df[types_df['Beverage Types'] == 'Spirits']
other = types_df[types_df['Beverage Types'] == 'Other alcoholic beverages']

sns.set_color_codes("pastel")

_ = plt.plot(beer["Year"], beer["Value"], color='r')
_ = plt.plot(wine["Year"], wine["Value"], color='g')
_ = plt.plot(spirits["Year"], spirits["Value"], color='b')
_ = plt.plot(other["Year"], other["Value"], color='m')

_ = plt.legend(('Beer', "Wine", 'Spirits', 'Other types'), loc='upper right')

#to show the plot or save it as a ong-file,, uncomment one of the next lines:

plt.savefig('visualizations/one_country/types_alcohol_compare_' + country_processed + '.png' , dpi=200)
plt.show()
plt.close()


# Compute ECDF for the chosen country
all_types = df[df['Beverage Types'] == 'All types']
x, y = ecdf(list(all_types.Value))

# Plot the ECDF
sns.set_color_codes("pastel")

_ = plt.plot(x, y, marker='.', linestyle='none', color='r')

# Set margins
#plt.margins(0.02)

# Add axis labels and legend

_ = plt.title('ECDF of alcohol consumption in 1960-2016 in ' + country)
_ = plt.xlabel('Alcohol consumption value')
_ = plt.ylabel('ECDF')

plt.savefig('visualizations/one_country/ecdf_' + country_processed + '.png' , dpi=200)
plt.show()
plt.close()
