import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams.update({'font.size': 20})

df = pd.read_csv('justicesdata2022.csv')

justice = df[['name']]
ideo = df[['ideo']]
yrnom = df[['yrnom']]

score = ideo.to_numpy()
year = yrnom.to_numpy()

have_data = score != '888. data unavailable'
x = np.asarray(year[have_data], dtype=int)
y = np.asarray(score[have_data], dtype=float)

true_data = y < 10

plt.scatter(x[true_data], y[true_data])
plt.title('Figure 1: Segal-Cover Scores of Supreme Court Justices')
plt.xlabel('Year of Appointment')
plt.ylabel('Segal-Cover Score')
plt.show()