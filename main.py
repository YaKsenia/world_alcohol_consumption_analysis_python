import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from draw_bootstrap_replications import bootstrap_replicate_1d, draw_bs_reps
from statistical_tests import hypothesis_test, ecdf, draw_bs_pairs, permutation_sample, draw_perm_reps, diff_of_means


df = pd.read_csv('alco_merge_full.csv')

print('Original size of data:', len(df))

df = df[['Country', 'Data Source_x', 'Beverage Types','2015', '2016']]
df = df.melt(id_vars=['Country', 'Data Source_x', 'Beverage Types'], 
        var_name="Year", 
        value_name="Value")

df = df[df['Value'] != 0.0]
types = ['All types', 'Beer', 'Wine', 'Spirits']

all_types = df[df['Beverage Types'] == 'All types']

#all_types = df[df['Year'] == '2016']


#all_types = all_types.dropna(how='any', inplace=True)
#print(all_types)
all_types = all_types.loc[all_types.Value.notnull()]

#print(all_types[all_types['Country'] == 'Austria'])

country = all_types.groupby('Country').sum().reset_index()

alco_leaders = country.nlargest(10, 'Value', keep='first')

leaders_list = list(alco_leaders['Country'])
leaders_all = df.loc[df['Country'].isin(leaders_list)]
leaders_all = leaders_all.groupby(['Country', 'Year']).mean().reset_index()
leaders_all = leaders_all.sort_values(by='Value')

sns.set_color_codes("pastel")
pivot = pd.pivot_table(leaders_all,  values='Value',  columns=['Year'],  
                         index = "Country", aggfunc=np.sum,  fill_value=0)
pivot = pivot.reindex(pivot.sort_values(by=['2016'], ascending=False).index)
pivot.plot(kind="bar")
plt.show()

print('Countries leaders in alcohol consumption:', alco_leaders)


for alco_type in types:

	print("Analysis for world consumption of this type of alcohol:", alco_type)
	print('\n')

	new_df = df[df['Beverage Types'] == alco_type]
	new_df = new_df.dropna()

	print('Sample size: ', len(new_df))

	data2015 = new_df[new_df['Year'] == '2015']
	data2016 = new_df[new_df['Year'] == '2016']
	
	print('Sample mean for 2015: ', data2015['Value'].mean())
	print('Sample median for 2015: ', data2015['Value'].median())
	print('Minumum value for 2015: ', data2015['Value'].min())
	print('Maximum value for 2015: ', data2015['Value'].max())

	print('Sample mean for 2016: ', data2016['Value'].mean())
	print('Sample median for 2016: ', data2016['Value'].median())
	print('Minumum value for 2016: ', data2016['Value'].min())
	print('Maximum value for 2016: ', data2016['Value'].max())

	# Compute ECDFs
	x_2015, y_2015 = ecdf(list(data2015.Value))
	x_2016, y_2016 = ecdf(list(data2016.Value))

	# Plot the ECDFs

	_ = plt.plot(x_2015, y_2015, marker='.', linestyle='none')
	_ = plt.plot(x_2016, y_2016, marker='.', linestyle='none')

	# Set margins
	plt.margins(0.02)

	# Add axis labels and legend
	_ = plt.xlabel('Alcohol consumption')
	_ = plt.ylabel('ECDF')
	_ = plt.legend(('2015','2016'), loc='lower right')

	# Show the plot
	#plt.savefig('ecdf_compare2015-2016_' + alco_type + '.png' , dpi=200)
	#plt.show()
	plt.close()

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

	# Print the results
	print('difference of means =', mean_diff)
	print('95% confidence interval =', conf_int)

	p_value = hypothesis_test(x_2015, x_2016, mean_diff)

	print('P-value with bootstrap replicates: ', p_value)

	empirical_diff_means = diff_of_means(x_2015, x_2016)

	# Draw 10,000 permutation replicates: perm_replicates
	perm_replicates = draw_perm_reps(x_2015, x_2016, diff_of_means, size=10000)

	# Compute p-value: p
	p_value2 = np.sum(perm_replicates <= empirical_diff_means) / len(perm_replicates)

	# Print the result
	print('P-value with permutation replicates:', p_value2)
	print('\n')