'''
Analysis with comparison of alcohol consumption between two years

This script processes the data, explores the data (EDA) with visualizations,
computes descriptive statistics of them and conducts hypothesis tests for each type of alcohol
to compare the data of alcohol consumption in _begin_year and _end_year.

'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from draw_bootstrap_replications import draw_bs_reps
from statistical_tests import hypothesis_test, ecdf, draw_perm_reps, diff_of_means
from config import filename
import argparse

# Define the parser
parser = argparse.ArgumentParser(description='Define the start and end year')

# Declare an argument (`--algo`), telling that the corresponding value should be stored in the `algo` field, and using a default value if the argument isn't given
parser.add_argument('--begin_year', action="store", dest='data1', default=1960)
parser.add_argument('--end_year', action="store", dest='data2', default=2016)

# Now, parse the command line arguments and store the values in the `args` variable
parse_years = parser.parse_args()

begin_year = str(parse_years.data1)
end_year = str(parse_years.data2)

#read the file

df = pd.read_csv(filename)

#keep only the columns which are necessary for the analysis

df = df[['Country', 'Beverage Types', begin_year, end_year]]

df['Beverage Types'] = df['Beverage Types'].replace({'Other alcoholic beverages': 'Other'})

#create a copy of the original dataframe
compare_years = df.copy()

#create a column with differences between _end_year and _begin_year alcohol consumption value
compare_years['diff'] = compare_years[end_year] - compare_years[begin_year]
compare_years = compare_years[compare_years['Beverage Types'] == 'All types']

#keep only values which are more than 0
compare_years = compare_years[compare_years[end_year] != 0.0]
compare_years = compare_years[compare_years[begin_year] != 0.0]

#create a column which tells if the alcohol consumption raised (1) or didn't raise (0)
compare_years['raise'] = np.where(compare_years['diff'] > 0, 1, 0)
compare_years = compare_years.dropna()

print('Number of countries where alcohol consumption in ' + end_year + ' raised: ', \
    len(compare_years[compare_years['raise'] == 1]))
print('Number of countries where alcohol consumption in ' + \
    end_year + ' dropped or didn\'t change: ',\
    len(compare_years[compare_years['raise'] == 0]), '\n')

#create new columns "Year" and 'Value' instead of two columns _begin_year and _end_year
df = df.melt(id_vars=['Country', 'Beverage Types'],
             var_name="Year",
             value_name="Value")

#remove rows where alcohol consumption value is 0
df = df[df['Value'] != 0.0]

#create a dataframe where the type of alcohol is only "All types"
all_types = df[df['Beverage Types'] == 'All types']

#delete rows with null values
all_types = all_types.loc[all_types.Value.notnull()]

#group the dataframe by Country and calculate sum of values for each country
country = all_types.groupby('Country').sum().reset_index()

#choose 10 countries where the sum of alcohol consumption for _begin_year-_end_year was the highest
alco_leaders = country.nlargest(10, 'Value', keep='first')

print('Countries leaders in alcohol consumption:', '\n', alco_leaders, '\n')

#create a list of 10 most 'alcoholic' countries'names
leaders_list = list(alco_leaders['Country'])

#use this list to choose from the main df only the rows with these countries
leaders = df.loc[df['Country'].isin(leaders_list)]

leaders = leaders[leaders['Beverage Types'] == 'All types']

leaders = leaders.loc[leaders.Value.notnull()]

#sns.set_color_codes("pastel")

#create a pivot table, so country becomes an index
pivot = pd.pivot_table(leaders, values='Value', columns=['Year'],
                       index="Country", aggfunc=np.sum, fill_value=0)

#sort values by _end_year alcohol value
pivot = pivot.reindex(pivot.sort_values(by=[end_year], ascending=False).index)

#create a visualization plot
pivot.plot(kind="bar")
plt.tight_layout()

#to show the plot or save it as a png-file, uncomment one of the next lines:

plt.savefig('visualizations/countries_leaders_begin_year-_end_year.png' , dpi=300)
plt.show()
plt.close()

types_df = df[df['Beverage Types'] != 'All types']
#create a pivot table, so beverage types becomes an index
pivot_type = pd.pivot_table(types_df, values='Value', columns=['Year'],
                            index="Beverage Types", aggfunc=np.sum, fill_value=0)

#sort values by _end_year alcohol value
pivot_type = pivot_type.reindex(pivot_type.sort_values(by=[end_year], ascending=False).index)

#create a visualization plot
pivot_type.plot(kind="bar")
plt.tight_layout()

#to show the plot or save it as a ong-file,, uncomment one of the next lines:

plt.savefig('visualizations/types_alcohol_compare_' + begin_year + '-' + end_year + '.png' , dpi=200)
plt.show()
plt.close()

df = df[df['Beverage Types'] != 'All types']
types = df['Beverage Types'].unique()
#['All types', 'Beer', 'Wine', 'Spirits']
results = pd.DataFrame(columns=['beverage_types', 'mean_' + begin_year, \
                       'mean_' + end_year, 'std_' + begin_year, 'std_' + end_year, \
                       'median_' + begin_year, 'median_' + end_year, 'min_' + begin_year, \
                       'min_' + end_year, 'max_' + begin_year, 'max_' + end_year,\
                       'p_bootstrap', 'p_permutation', 'significant_change'])
#go through every type of alcohol in the data and analyse it separately

fig1 = plt.figure(figsize=(16, 8))
fig2 = plt.figure(figsize=(16, 8))
columns = 4
rows = 1
for i, alco_type in enumerate(types):

    i = i + 1
    print("Analysis for world consumption of this type of alcohol:", alco_type)
    print('\n')

    #make a new temporary dataframe with only this type of alcohol
    new_df = df[df['Beverage Types'] == alco_type]
    new_df = new_df.dropna()

    print('Sample size: ', len(new_df))

    #make two different dataframes for _begin_year and _end_year
    data_begin_year = new_df[new_df['Year'] == begin_year]
    data_end_year = new_df[new_df['Year'] == end_year]

    #calculate descriptive statistics
    mean_begin_year = data_begin_year['Value'].mean()
    mean_end_year = data_end_year['Value'].mean()

    std_begin_year = data_begin_year['Value'].std()
    std_end_year = data_end_year['Value'].std()

    median_begin_year = data_begin_year['Value'].median()
    median_end_year = data_end_year['Value'].median()

    min_begin_year = data_begin_year['Value'].min()
    min_end_year = data_end_year['Value'].min()

    max_begin_year = data_begin_year['Value'].max()
    max_end_year = data_end_year['Value'].max()

    print('Sample mean for ' + begin_year + ': ', mean_begin_year)
    print('Sample mean for ' + end_year + ': ', mean_end_year)

    print('Sample median for ' + begin_year + ': ', median_begin_year)
    print('Sample median for ' + end_year + ': ', median_end_year)

    print('Sample STD for ' + begin_year + ': ', std_begin_year)
    print('Sample STD for ' + end_year + ': ', std_end_year)

    print('Minumum value for ' + begin_year + ': ', min_begin_year)
    print('Minumum value for ' + end_year + ': ', min_end_year)

    print('Maximum value for ' + begin_year + ': ', max_begin_year)
    print('Maximum value for ' + end_year + ': ', max_end_year)

    # Compute ECDFs for _begin_year and _end_year

    x_begin_year, y_begin_year = ecdf(list(data_begin_year.Value))
    x_end_year, y_end_year = ecdf(list(data_end_year.Value))

    # Plot the ECDFs


    axis1 = fig1.add_subplot(rows, columns, i)
    axis1.set_title('ECDF of ' + alco_type.lower() + ' consumption')



    axis1.plot(x_begin_year, y_begin_year, marker='.', linestyle='none')
    axis1.plot(x_end_year, y_end_year, marker='.', linestyle='none')

    # Set margins
    #plt.margins(0.02)

    # Add axis labels and legend
    axis1.set_xlabel('Alcohol consumption value')
    axis1.set_ylabel('ECDF')
    #axis1.set_legend((begin_year,end_year), loc='lower right')

    #Swarmplot


    # Label axes

    #fig2.add_subplot(rows, columns, i)

    axis2 = fig2.add_subplot(rows, columns, i)
    axis2 = sns.swarmplot(x='Year', y='Value', data=new_df)
    axis2.set_title('Consumption of ' + alco_type.lower())

    # Compute two hypothesis tests - based on bootstrap replicates and permutation replicates
    # The hypothesis is: World alcohol consumption in _end_year raised
    #significatly comparing to _begin_year
    # Null hypothesis: There was no significant change in world alcohol consumption

    print('\n', 'Hypothesis test for', alco_type, '\n')

    # Compute the difference of the sample means: mean_diff
    mean_diff = diff_of_means(x_end_year, x_begin_year)

    # Get bootstrap replicates of means
    bs_replicates_begin_year = draw_bs_reps(x_begin_year, np.mean, size=10000)
    bs_replicates_end_year = draw_bs_reps(x_end_year, np.mean, size=10000)

    # Compute bootstrap samples of difference of means: bs_diff_replicates
    bs_diff_replicates = bs_replicates_end_year - bs_replicates_begin_year

    # Compute 95% confidence interval: conf_int
    conf_int = np.percentile(bs_diff_replicates, [2.5, 97.5])

    print('difference of means =', mean_diff)
    print('95% confidence interval for differences of means =', conf_int)

    p_value = hypothesis_test(x_begin_year, x_end_year, mean_diff)

    print('P-value with bootstrap replicates: ', p_value)

    mean_diff_permutation = diff_of_means(x_begin_year, x_end_year)

    # Draw 10,000 permutation replicates: perm_replicates
    perm_replicates = draw_perm_reps(x_begin_year, x_end_year, diff_of_means, size=10000)

    # Compute p-value: p
    p_value2 = np.sum(perm_replicates <= mean_diff_permutation) / len(perm_replicates)

    # Print the result
    print('P-value with permutation replicates:', p_value2)
    print('\n')

    if p_value <= 0.05 and p_value2 <= 0.05:

        significant_change = 'raise'

    elif p_value >= 0.95 and p_value2 >= 0.95:

        significant_change = 'drop'

    else:

        significant_change = 'no'

    results.loc[i] = [alco_type] + [mean_begin_year] + [mean_end_year] + [std_begin_year]\
    + [std_end_year] +[median_begin_year] + [median_end_year] + [min_begin_year] +\
    [min_end_year] + [max_begin_year] + [max_end_year] + [p_value] + [p_value2] +\
    [significant_change]

# save the figures with plots or just show them (uncomment your preference)

#fig1.savefig('visualizations/ecdfs_begin_year-_end_year.png' , dpi=200)
#fig2.savefig('visualizations/swarmplots_begin_year-_end_year.png' , dpi=200)

plt.show()

results.to_csv('statistics_results.csv')
