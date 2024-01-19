import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# only works in the same directory
def get_csv_data_local(filename):
    file_path = os.path.join(os.path.dirname(__file__), filename)
    data = pd.read_csv(file_path)
    return data

def extract_xyz_arrays(data):
    x_values = data['carPositionX'].to_numpy()
    y_values = data['carPositionY'].to_numpy()
    z_values = data['carPositionZ'].to_numpy()
    return x_values, y_values, z_values

def plot_xyz(x_values, y_values, z_values):
    plt.style.use('dark_background')
    plt.scatter(x_values, y_values, c=z_values, cmap='RdYlGn', marker='o', label='Data')
    cbar = plt.colorbar()
    cbar.set_label('Z Values')
    plt.xlabel('X Values')
    plt.ylabel('Y Values')
    plt.title('Terrain')
    plt.show()

csv_data = get_csv_data_local('creampie.csv')
x_values, y_values, z_values = extract_xyz_arrays(csv_data)
plot_xyz(x_values, y_values, z_values)
