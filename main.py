'''
This script processes the data, explores the data (EDA) with visualizations, 
computes descriptive statistics of them and conducts hypothesis tests for each type of alcohol

'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from draw_bootstrap_replications import bootstrap_replicate_1d, draw_bs_reps
from statistical_tests import hypothesis_test, ecdf, draw_bs_pairs, permutation_sample, draw_perm_reps, diff_of_means

#pd.set_option('display.max_rows', df.shape[0]+1)

#read the file 

df = pd.read_csv('data_world_alcohol_consumption.csv')

print('Number of rows and columns of the data:', df.shape)

#keep only the columns which are necessary for the analysis

df = df[['Country', 'Beverage Types','2015', '2016']]

#create a copy of the original dataframe
compare_years = df.copy()

#create a column with differences between 2016 and 2015 alcohol consumption value
compare_years['diff'] = compare_years['2016'] - compare_years['2015']

#keep only values which are more than 0
compare_years = compare_years[compare_years['2016'] != 0.0]
compare_years = compare_years[compare_years['2015'] != 0.0]

#create a column which tells if the alcohol consumption raised (1) or didn't raise (0)
compare_years['raise'] = np.where(compare_years['diff'] > 0, 1, 0)
compare_years = compare_years.dropna()

print('Number of countries where alcohol consumption in 2016 raised:', len(compare_years[compare_years['raise'] == 1]))
print('Number of countries where alcohol consumption in 2016 dropped or didn\'t change:', len(compare_years[compare_years['raise'] == 0]), '\n')

#create new columns "Year" and 'Value' instead of two columns 2015 and 2016
df = df.melt(id_vars=['Country', 'Beverage Types'], 
        var_name="Year", 
        value_name="Value")

#remove rows where alcohol consumption value is 0
df = df[df['Value'] != 0.0]

#create a dataframe where the type of alcohol is only "All types"

all_types = df[df['Beverage Types'] == 'All types']

print('Statistics of the "Value" column: ', '\n', all_types.Value.describe(), '\n')

#delete rows with null values

all_types = all_types.loc[all_types.Value.notnull()]

#group the dataframe by Country and calculate sum of values for each country

country = all_types.groupby('Country').sum().reset_index()

#choose 10 countries where the sum of alcohol consumption for 2015-2016 was the highest

alco_leaders = country.nlargest(10, 'Value', keep='first')

print('Countries leaders in alcohol consumption:', '\n', alco_leaders, '\n')

#create a list of 10 most 'alcoholic' countries'names

leaders_list = list(alco_leaders['Country'])

#use this list to choose from the main df only the rows with these countries

leaders = df.loc[df['Country'].isin(leaders_list)]

#group by country name and year (so we get every country's alcohol value twice - for 2015 and 2016
leaders = leaders.groupby(['Country', 'Year']).mean().reset_index()
#leaders = leaders.sort_values(by='Value')

#sns.set_color_codes("pastel")

#create a pivot table, so country becomes an index
pivot = pd.pivot_table(leaders,  values='Value',  columns=['Year'],  
                         index = "Country", aggfunc=np.sum,  fill_value=0)

#sort values by 2016 alcohol value
pivot = pivot.reindex(pivot.sort_values(by=['2016'], ascending=False).index)

#create a visualization plot
pivot.plot(kind="bar")
plt.tight_layout()

#to show the plot or save it as a ong-file,, uncomment one of the next lines:

#plt.savefig('countries_leaders_2015-2016.png' , dpi=300)
#plt.show()
plt.close()

types_df = df[df['Beverage Types'] != 'All types']
#create a pivot table, so beverage types becomes an index
pivot_type = pd.pivot_table(types_df,  values='Value',  columns=['Year'],  
                         index = "Beverage Types", aggfunc=np.sum,  fill_value=0)

#sort values by 2016 alcohol value
pivot_type = pivot_type.reindex(pivot_type.sort_values(by=['2016'], ascending=False).index)

#create a visualization plot
pivot_type.plot(kind="bar")
plt.tight_layout()

#to show the plot or save it as a ong-file,, uncomment one of the next lines:

#plt.savefig('types_alcohol_compare_2015-2016.png' , dpi=200)
#plt.show()
plt.close()


types = df['Beverage Types'].unique()
#['All types', 'Beer', 'Wine', 'Spirits']

#go through every type of alcohol in the data and analyse it separately
for alco_type in types:

	print("Analysis for world consumption of this type of alcohol:", alco_type)
	print('\n')

	#make a new temporary dataframe with only this type of alcohol
	new_df = df[df['Beverage Types'] == alco_type]
	new_df = new_df.dropna()

	print('Sample size: ', len(new_df))

	#make two different dataframes for 2015 and 2016
	data2015 = new_df[new_df['Year'] == '2015']
	data2016 = new_df[new_df['Year'] == '2016']
	
	#calculate descriptive statistics
	print('Sample mean for 2015: ', data2015['Value'].mean())
	print('Sample mean for 2016: ', data2016['Value'].mean())

	print('Sample median for 2015: ', data2015['Value'].median())
	print('Sample median for 2016: ', data2016['Value'].median())

	print('Sample STD for 2015: ', data2015['Value'].std())
	print('Sample STD for 2016: ', data2016['Value'].std())

	print('Minumum value for 2015: ', data2015['Value'].min())
	print('Minumum value for 2016: ', data2016['Value'].min())

	print('Maximum value for 2015: ', data2015['Value'].max())
	print('Maximum value for 2016: ', data2016['Value'].max())

	# Compute ECDFs for 2015 and 2016

	x_2015, y_2015 = ecdf(list(data2015.Value))
	x_2016, y_2016 = ecdf(list(data2016.Value))

	# Plot the ECDFs

	_ = plt.plot(x_2015, y_2015, marker='.', linestyle='none')
	_ = plt.plot(x_2016, y_2016, marker='.', linestyle='none')

	# Set margins
	plt.margins(0.02)

	# Add axis labels and legend
	_ = plt.xlabel('Alcohol consumption of ' + alco_type.lower())
	_ = plt.ylabel('ECDF')
	_ = plt.legend(('2015','2016'), loc='lower right')

	# Show the plot or save it to a file (ucomment what you want to do)

	plt.savefig('ecdf_compare_2015-2016_' + alco_type + '.png' , dpi=200)
	#plt.show()
	plt.close()

	# Compute two hypothesis tests - based on bootstrap replicates and permutation replicates
	# The hypothesis is: World alcohol consumption in 2016 raised significatly comparing to 2015
	# Null hypothesis: There was no significant change in world alcohol consumption

	print('\n', 'Hypothesis test for', alco_type, '\n')
	
	# Compute the difference of the sample means: mean_diff
	mean_diff = diff_of_means(x_2016, x_2015)

	# Get bootstrap replicates of means
	bs_replicates_2015 = draw_bs_reps(x_2015, np.mean, size=10000)
	bs_replicates_2016 = draw_bs_reps(x_2016, np.mean, size=10000)

	# Compute bootstrap samples of difference of means: bs_diff_replicates
	bs_diff_replicates = bs_replicates_2016 - bs_replicates_2015

	# Compute 95% confidence interval: conf_int
	conf_int = np.percentile(bs_diff_replicates, [2.5, 97.5])

	print('difference of means =', mean_diff)
	print('95% confidence interval for differences of means =', conf_int)

	p_value = hypothesis_test(x_2015, x_2016, mean_diff)

	print('P-value with bootstrap replicates: ', p_value)

	mean_diff_permutation = diff_of_means(x_2015, x_2016)

	# Draw 10,000 permutation replicates: perm_replicates
	perm_replicates = draw_perm_reps(x_2015, x_2016, diff_of_means, size=10000)

	# Compute p-value: p
	p_value2 = np.sum(perm_replicates <= mean_diff_permutation) / len(perm_replicates)

	# Print the result
	print('P-value with permutation replicates:', p_value2)
	print('\n')