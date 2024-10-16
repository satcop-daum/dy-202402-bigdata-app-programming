
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
   'pig': [20, 18, 489, 675, 1776],
   'horse': [4, 25, 281, 600, 1900]
   }, index=[1990, 1997, 2003, 2009, 2014])
df.plot.line()

plt.show()

