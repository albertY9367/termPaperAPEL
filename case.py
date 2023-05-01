import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams.update({'font.size': 20})

df = pd.read_csv('bonica_sen_fed_judges.csv')

seq = np.arange(-2, 2, 0.1)

presi = df[['president.name']]
cfscore = df[['imputed.dime.cfscore']]

presi = presi.to_numpy()
cfscore = cfscore.to_numpy()

ford = presi == 'Gerald Ford'
carter = presi == 'Jimmy Carter'
reagan = presi == 'Ronald Reagan'
bush1 = presi == 'George H.W. Bush'
clinton = presi == 'William J. Clinton'
bush2 = presi == 'George W. Bush'
obama = presi == 'Barack Obama'

notnan = np.logical_not(np.isnan(cfscore))
ford = np.logical_and(ford, notnan)
carter = np.logical_and(carter, notnan)
reagan = np.logical_and(reagan, notnan)
bush1 = np.logical_and(bush1, notnan)
clinton = np.logical_and(clinton, notnan)
bush2 = np.logical_and(bush2, notnan)
obama = np.logical_and(obama, notnan)

plt.hist(cfscore[obama], bins=seq, range=(-2, 2))

plt.title('Figure 4: Federal Judges Ideology Distribution Under Different Presidents \n \n Barack Obama')
plt.show()



