import pandas as pd
import numpy as np
from ecdf import ecdf
import matplotlib.pyplot as plt
import seaborn as sns
from draw_bootstrap_replications import bootstrap_replicate_1d, draw_bs_reps
from hypothesis_test import hypothesis_test


def diff_of_means(data_1, data_2):
    """Difference in means of two arrays."""

    # The difference of means of data_1, data_2: diff
    diff = np.mean(data_1) - np.mean(data_2)

    return diff



df = pd.read_csv('alco_merge_full.csv')

print('Original size of data:', len(df))

df = df[['Country', 'Data Source_x', 'Beverage Types','2015', '2016']]
df = df.melt(id_vars=['Country', 'Data Source_x', 'Beverage Types'], 
        var_name="Year", 
        value_name="Value")

types = ['All types', 'Beer', 'Wine', 'Spirits']

for alco_type in types:

	print("Analysis for this type of alcohol:", alco_type)
	print('\n')

	new_df = df[df['Beverage Types'] == alco_type]
	new_df = new_df.dropna()
	print('Sample size: ', len(new_df))

	data2016 = new_df[new_df['Year'] == '2016']
	data2015 = new_df[new_df['Year'] == '2015']

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
	plt.savefig('ecdf_compare2015-2016_' + alco_type + '.png' , dpi=200)
	plt.close()
	#plt.show()

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

	print('P-value', p_value)
	print('\n')