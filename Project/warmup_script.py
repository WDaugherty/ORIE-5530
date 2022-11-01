#Import Libraries
import numpy as np #Mathematical Operations
import matplotlib.pyplot as pl #Visualizations
import pandas as pd #Dataframe manipulation
import datetime as dt #Datatime manipulation

#Load in the data
df = pd.read_csv("/Users/wdaugherty/ORIE-5530/ORIE-5530/Project/202207-citbike-tripdata.csv", delimiter=",")

#print checkpoint
print(df.head())