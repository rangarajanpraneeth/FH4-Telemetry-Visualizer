import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# only works in the same directory
def get_csv_data_local(filename):
    file_path = os.path.join(os.path.dirname(__file__), filename)
    data = pd.read_csv(file_path)
    return data

def extract_xyz_arrays(data):
    x_values = data['x'].to_numpy()
    y_values = data['y'].to_numpy()
    z_values = data['z'].to_numpy()
    return x_values, y_values, z_values

def plot_xy(x_values, y_values):
    plt.plot(x_values, y_values, marker='o', linestyle='-', color='b', label='Data')
    plt.xlabel('X Values')
    plt.ylabel('Y Values')
    plt.title('X vs Y Plot')
    plt.legend()
    plt.show()

csv_data = get_csv_data_local('creampie.csv')
x_values, y_values, z_values = extract_xyz_arrays(csv_data)
plot_xy(x_values, y_values)
