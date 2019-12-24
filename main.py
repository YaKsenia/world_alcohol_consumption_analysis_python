'''
ECDFs of beak depths

While bee swarm plots are useful, we found that ECDFs are often even better when doing EDA. Plot the ECDFs for the 1975 and 2012 beak depth measurements on the same plot.

For your convenience, the beak depths for the respective years has been stored in the NumPy arrays data2016 and data2015.

'''
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



df = pd.read_csv('/home/ksenia_new/my_project/alco_merge_full.csv')
print(len(df))
#print(df.columns)
#df = df.dropna(subset=['PERCENTAGE_URBAN_POPULATION', 'FEMALE_LITERACY'])
#print(len(df))
df = df[df['Beverage Types'] == 'All types']

'''
df = df[['Country', 'Data Source_x', 'Beverage Types', '2016',
        '2015', '2013', '2012', '2011', '2010', '2009', '2008', '2007',
       '2006', '2005', '2004', '2003', '2002', '2000']]
'''
df = df[['Country', 'Data Source_x', 'Beverage Types','2015', '2016']]

df = df.melt(id_vars=['Country', 'Data Source_x', 'Beverage Types'], 
        var_name="Year", 
        value_name="Value")

df = df.dropna()
data2016 = df[df['Year'] == '2016']
data2015 = df[df['Year'] == '2015']


# Compute ECDFs
x_2016, y_2016 = ecdf(list(data2016.Value))
x_2015, y_2015 = ecdf(list(data2015.Value))

#data2016 = np.array(df[df['Year'] == '2016'])
#data2015 = np.array(df[df['Year'] == '2015'])


# Plot the ECDFs
_ = plt.plot(x_2016, y_2016, marker='.', linestyle='none')
_ = plt.plot(x_2015, y_2015, marker='.', linestyle='none')

# Set margins
plt.margins(0.02)

# Add axis labels and legend
_ = plt.xlabel('Alcohol consumption')
_ = plt.ylabel('ECDF')
_ = plt.legend(('2016', '2015'), loc='lower right')

# Show the plot
#plt.savefig('ecdf_compare2015-2016.png' , dpi=200)
plt.show()

# Compute the difference of the sample means: mean_diff
mean_diff = diff_of_means(x_2016, x_2015)

# Get bootstrap replicates of means
bs_replicates_2016 = draw_bs_reps(x_2016, np.mean, size=10000)
bs_replicates_2015 = draw_bs_reps(x_2015, np.mean, size=10000)
#print(bs_replicates_2016)
# Compute samples of difference of means: bs_diff_replicates
bs_diff_replicates = bs_replicates_2016 - bs_replicates_2015

# Compute 95% confidence interval: conf_int
conf_int = np.percentile(bs_diff_replicates, [2.5, 97.5])

# Print the results
print('difference of means =', mean_diff)
print('95% confidence interval =', conf_int)
#plt.show()

p_value = hypothesis_test(x_2016, x_2015, mean_diff)
print(p_value)