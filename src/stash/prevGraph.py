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
    plt.scatter(data['carPositionX'], data['carPositionY'], c=cVal, cmap='RdYlGn_r', marker='o', label='Data')
    cbar = plt.colorbar()
    cbar.set_label(val)
    plt.xlabel('X Values')
    plt.ylabel('Y Values')
    plt.title(val)
    plt.show()

plot_cVal('creampie.csv', 'carSpeed')









# import os
# import pandas as pd
# import matplotlib.pyplot as plt


# def graph3D(filePath, colorProperty):
#     dataFrame = pd.read_csv(
#         os.path.abspath(os.path.join(os.path.dirname(__file__), "../data", filePath))
#     )
#     plt.style.use("dark_background")
#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection="3d")
#     ax.xaxis.set_pane_color((0, 0, 0))
#     ax.yaxis.set_pane_color((0, 0, 0))
#     ax.zaxis.set_pane_color((0, 0, 0))
#     ax.scatter(
#         dataFrame["carPositionX"],
#         dataFrame["carPositionZ"],
#         dataFrame["carPositionY"],
#         # c="r",
#         c=dataFrame[colorProperty],
#         cmap="RdYlGn_r",
#     )
#     ax.axis("equal")
#     plt.show()


# graph3D("recording-1.csv", "carSpeed")
