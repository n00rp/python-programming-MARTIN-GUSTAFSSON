import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

#Uppgift 1 c)

#Samtling av funktioner för datahandling Excercise_01




def plot_missing_values(df):
    missing_values = df.isnull().sum()
    missing_values = missing_values[missing_values > 0]
    if len(missing_values) > 0:
        colors = plt.cm.tab20(np.arange(len(missing_values)) / len(missing_values))
        missing_values.plot(kind="bar", color=colors)
        plt.title('Missing Values')
        plt.xlabel('Column')
        plt.ylabel('Number of Missing Values')
        plt.show()
    else:
        print("No missing values found in the DataFrame.")