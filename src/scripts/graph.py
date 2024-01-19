# import json
# import os
# import numpy as np
# import matplotlib.pyplot as plt

# def get_file_path(file):   
#     current_directory = os.path.dirname(os.path.abspath(__file__))
#     database_directory = os.path.join(current_directory, '..', '..', 'database')
#     file_path = os.path.join(database_directory, file)
#     return file_path

# def getJSON(file_name):
#     with open(get_file_path(file_name), 'r') as file:
#         data = json.load(file)
#     return data

# def uploadJSON(file_name, data):
#     file_path = get_file_path(file_name)
#     with open(file_path, 'w') as file:
#         json.dump(data, file, indent=2)
#     print(f"Data successfully uploaded to '{file_path}'.")


# x = np.linspace(0, 10, 100)  # Create an array of 100 points from 0 to 10
# y = np.sin(x)  # Compute the sine values for each x

# # Plot the data using Matplotlib
# plt.plot(x, y, label='Sine Curve')
# plt.title('Sine Curve Example')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.legend()  # Show legend
# plt.grid(True)  # Show grid
# plt.show()  # Display the plot


# # 








import os
import pandas as pd

def get_csv_data_local(filename):
    file_path = os.path.join(os.path.dirname(__file__), filename)
    data = pd.read_csv(file_path)
    return data

# Example usage:
# Assuming you have a CSV file named 'creampie.csv' in the same directory as this script
filename = 'creampie.csv'
csv_data = get_csv_data_local(filename)

if csv_data is not None:
    print(f"CSV data from '{filename}':")
    print(csv_data)

