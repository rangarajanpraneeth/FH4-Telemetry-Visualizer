import os
import pandas as pd
import matplotlib.pyplot as plt

# only works in the same directory
def get_csv_data_local(filename):
    return pd.read_csv(os.path.join(os.path.dirname(__file__), filename))

def extract_csv(data):
    return {column: data[column].to_numpy() for column in data.columns[data.notna().any()].tolist()}

def plot_space_cVal(fileName, val, vtype):
    data = extract_csv(get_csv_data_local(fileName))
    cVal = data[val]
    plt.style.use('dark_background')
    if vtype == 'space':
        plt.axis('equal')
        plt.scatter(data['carPositionX'], data['carPositionZ'], c=cVal, cmap='RdYlGn_r', marker='o', label='Data')
        plt.xlabel('X-Direction')
        plt.ylabel('Y-Direction')
    elif vtype == 'time':
        timestampArr = data['timestamp']
        initialTime = timestampArr[0]
        for i in range(len(timestampArr)):
            timestampArr[i] = timestampArr[i] - initialTime
        plt.style.use('dark_background')
        plt.scatter(timestampArr,cVal ,c=cVal, cmap='RdYlGn_r', marker='o', label='Data')
        plt.xlabel('Time')
        plt.ylabel(val)
    else:
        print('Wrong Parameter passed')
    cbar = plt.colorbar()
    cbar.set_label(val)
    plt.title(val)
    plt.show()

plot_space_cVal('creampie.csv', 'carSpeed', 'space')
