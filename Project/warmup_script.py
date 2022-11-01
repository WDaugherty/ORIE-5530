
import numpy as np #Mathematical Operations
import matplotlib.pyplot as pl #Visualizations
import pandas as pd #Dataframe manipulation
import datetime as dt #Datatime manipulation


df = pd.read_csv("/Users/wdaugherty/ORIE-5530/ORIE-5530/Project/202207-citbike-tripdata.csv", delimiter=",") #Load in the data

#Writes a file that explores the data 
with open("Data_Descriptions.txt","a") as f:
    print(df.head(), file=f)
    print(df.describe(), file=f)

 #Describes the data

#Prints out durations longer than 3 hours
durations = []
for index, row in df.iterrows():
    start = dt.strptime((row["started_at"]), "%Y-%m-%d %H:%M:%S")
    end = dt.strptime((row["ended_at"]), "%Y-%m-%d %H:%M:%S")
    durations.append((end-start).total_seconds() / 60)
    
    if len(durations) % 200000 == 0:
        print(len(durations))


#Filters out the data longer than 3 hours 

df['duration'] = durations
durations_df=df[df['duration']<=200]
durations_df = durations_df[durations_df['duration']>=0]

