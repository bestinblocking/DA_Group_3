import pandas as pd
import xlrd
import numpy as np
import matplotlib.pyplot as plt





cols = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18] # To call out the whole countries of asia which has 18 columns
row = [241] # Start reading the excel file from row 241
df = pd.read_excel('IMVA.xlsx', sheet_name='IMVA') # to read the excel file
pd.set_option('display.max_columns', 18) # to preview the whole 18 columns, if delete there will be semi colons
pd.set_option('display.max_rows', 361) # to preview the whole of 361 rows, if delete it wont preview the whole 361 rows
pd.set_option('display.max_colwidth', 1000)  # the start printing from rows 241 to 361 and from 1 to 18

ranges = (df.iloc[240:361, :18]) # the start printing from rows 241 to 361 and from 1 to 18
calculated = (df.iloc[240:361, 1:19].sum(axis=0)) # Sum of whole value from 241-361 & from 1-18
top3 = (df.iloc[240:361, 1:19].sum(axis=0).nlargest(3))# Print out top 3 largest value country using n.largest


# pie chart
labels = [' Indonesia ', ' Japan ', ' China ']  # Data to plot
values = [15094895, 6908915, 6809539] # Inserting values of top 3 countries to chart
colors = ['lightskyblue', 'lightcoral', 'yellowgreen'] # Colors of pie chart
explode = (0.1, 0, 0) # Largest value will be sliced out
plt.pie(values, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=110 ) # styles for pie chart and % value and angle
plt.title('Top 3 Countries', fontsize= 18) # piechart title
plt.axis('equal') # to make it to a fixed circle
plt.legend(labels) # Print out labels at the top right
plt.tight_layout() # to make the pie chart compact
plt.savefig("Top3_pie.png")


ax = ranges [[' Japan ', ' Indonesia ', ' China ']].plot(kind='bar', title = "Top 3 Countries", figsize=(20, 20), legend=True, fontsize=10)
plt.savefig("Top3_bar.png")
print(ranges)
print(calculated)
print(top3)



