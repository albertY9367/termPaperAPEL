import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams.update({'font.size': 20})
# read the csv file
df = pd.read_csv('justices.csv')

# move to numpy array format
term = df[['term']]
justice = df[['justice']]
post_mn = df[['post_mn']]
term.to_numpy()
justice.to_numpy()
post_mn.to_numpy()

time_stat = np.array([])

if False:
    
    for i in np.arange(np.min(term), np.max(term)+1):
        
        isyear = np.isclose(term, i)
        # sqval = np.sum(np.square(post_mn[isyear]))/np.count_nonzero(isyear)
        absval = np.sum(np.abs(post_mn[isyear]))/np.count_nonzero(isyear)
        time_stat = np.append(time_stat, absval)
    
    year_arr = np.arange(1937, 2022)
    plt.plot(year_arr, time_stat, label='Data')
    
    k, b = np.polyfit(year_arr, time_stat, deg=1)
    plt.plot(year_arr, k*year_arr + b, label='Linear Fit')
    plt.title('Figure 3: Time Evolution of M-Q Polarization Measurement')
    plt.xlabel('Term')
    plt.ylabel('Ideological Polarization Measurement')
    plt.legend()
    plt.show()
    
    
if True:
    # plot the ideological change of each justice
    for i in np.arange(np.min(justice), np.max(justice)+1):
        
        isjust = np.isclose(justice, i)
        plt.plot(term[isjust], post_mn[isjust])
        
    plt.title('Figure 2: Time Evolution of Martin-Quinn Scores of Supreme Court Justices')
    plt.xlabel('Term')
    plt.ylabel('Estimated Ideal Point')
    plt.show()

