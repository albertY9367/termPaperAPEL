import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('casevote.csv')

caseId = df[['caseId']]
majvote = df[['majVotes']]
minvote = df[['minVotes']]

caseId = caseId.to_numpy()
majvote = majvote.to_numpy()
minvote = minvote.to_numpy()


