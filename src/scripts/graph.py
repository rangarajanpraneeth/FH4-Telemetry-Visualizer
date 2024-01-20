import os
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# only works in the same directory
def get_csv_data_local(filename):
    return pd.read_csv(os.path.join(os.path.dirname(__file__), filename))

def extract_csv(data):
    return {column: data[column].to_numpy() for column in data.columns[data.notna().any()].tolist()}

def plot_space_cVal(fileName, val, type):
    data = extract_csv(get_csv_data_local(fileName))
    cVal = data[val]
    plt.style.use('dark_background')
    if type == 'space':
        plt.axis('equal')
        plt.scatter(data['carPositionX'], data['carPositionZ'], c=cVal, cmap='RdYlGn_r', marker='o', label='Data')
        plt.xlabel('X-Direction')
        plt.ylabel('Y-Direction')
    elif type == 'time':
        timestampArr = data['timestamp']
        initialTime = timestampArr[0]
        for i in range(len(timestampArr)):
            timestampArr[i] = timestampArr[i] - initialTime
        plt.scatter(timestampArr,cVal ,c=cVal, cmap='RdYlGn_r', marker='o', label='Data')
        plt.xlabel('Time')
        plt.ylabel(val)
    else:
        print('Wrong Parameter passed')
    cbar = plt.colorbar()
    cbar.set_label(val)
    plt.title(val)
    plt.show()

def plot_3d_graph(x, y, z):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
        # ax.set_aspect('equal')
        # ax.set_ylim(-1000,1000)
    # Scatter plot
    ax.scatter(x, y, z, c='r', marker='o')

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    # ax.set_aspect('equal')
    ax.axis('equal')
    
    # ax.set_box_aspect([1, 1, 1], adjustable='box')

    plt.show()

plot_space_cVal('creampie.csv', 'carPositionY', 'space')

# Example data
# x_data = [1, 2, 3, 4, 5]
# y_data = [2, 3, 4, 5, 6]
# z_data = [5, 6, 7, 8, 9]

# Plot the 3D graph
data = extract_csv(get_csv_data_local('creampie.csv'))
plot_3d_graph(data['carPositionX'], data['carPositionY'], data['carPositionZ'])
