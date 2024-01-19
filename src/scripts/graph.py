import os
import pandas as pd
import matplotlib.pyplot as plt

# only works in the same directory
def get_csv_data_local(filename):
    return pd.read_csv(os.path.join(os.path.dirname(__file__), filename))

def extract_csv(data):
    return {column: data[column].to_numpy() for column in data.columns[data.notna().any()].tolist()}

def plot_cVal(fileName, val):
    data = extract_csv(get_csv_data_local(fileName))
    cVal = data[val]
    plt.style.use('dark_background')
    plt.scatter(data['carPositionX'], data['carPositionY'], c=cVal, cmap='RdYlGn', marker='o', label='Data')
    cbar = plt.colorbar()
    cbar.set_label('cVal')
    plt.xlabel('X Values')
    plt.ylabel('Y Values')
    plt.title(val)
    plt.show()

plot_cVal('creampie.csv', 'inputGear')
