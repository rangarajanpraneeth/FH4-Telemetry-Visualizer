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

def extract_csv(data):
    non_empty_columns = data.columns[data.notna().any()].tolist()
    return {column: data[column].to_numpy() for column in non_empty_columns}

# def extract_csv(data):
#     inRace = data['inRace'].to_numpy()
#     timestamp = data['timestamp'].to_numpy()
#     engineMaxRPM = data['engineMaxRPM'].to_numpy()
#     engineIdleRPM = data['engineIdleRPM'].to_numpy()
#     engineRPM = data['engineRPM'].to_numpy()
#     carAccelerationX = data['carAccelerationX'].to_numpy()
#     carAccelerationY = data['carAccelerationY'].to_numpy()
#     carAccelerationZ = data['carAccelerationZ'].to_numpy()
#     carVelocityX = data['carVelocityX'].to_numpy()
#     carVelocityY = data['carVelocityY'].to_numpy()
#     carVelocityZ = data['carVelocityZ'].to_numpy()
#     carAngularVelocityX = data['carAngularVelocityX'].to_numpy()
#     carAngularVelocityY = data['carAngularVelocityY'].to_numpy()
#     carAngularVelocityZ = data['carAngularVelocityZ'].to_numpy()
#     carYaw = data['carYaw'].to_numpy()
#     carPitch = data['carPitch'].to_numpy()
#     carRoll = data['carRoll'].to_numpy()
#     suspensionTravelNormalizedFL = data['suspensionTravelNormalizedFL'].to_numpy()
#     suspensionTravelNormalizedFR = data['suspensionTravelNormalizedFR'].to_numpy()
#     suspensionTravelNormalizedRL = data['suspensionTravelNormalizedRL'].to_numpy()
#     suspensionTravelNormalizedRR = data['suspensionTravelNormalizedRR'].to_numpy()
#     tireSlipRatioFL = data['tireSlipRatioFL'].to_numpy()
#     tireSlipRatioFR = data['tireSlipRatioFR'].to_numpy()
#     tireSlipRatioRL = data['tireSlipRatioRL'].to_numpy()
#     tireSlipRatioRR = data['tireSlipRatioRR'].to_numpy()
#     wheelRotationSpeedFL = data['wheelRotationSpeedFL'].to_numpy()
#     wheelRotationSpeedFR = data['wheelRotationSpeedFR'].to_numpy()
#     wheelRotationSpeedRL = data['wheelRotationSpeedRL'].to_numpy()
#     wheelRotationSpeedRR = data['wheelRotationSpeedRR'].to_numpy()
#     wheelOnRumbleFL = data['wheelOnRumbleFL'].to_numpy()
#     wheelOnRumbleFR = data['wheelOnRumbleFR'].to_numpy()
#     wheelOnRumbleRL = data['wheelOnRumbleRL'].to_numpy()
#     wheelOnRumbleRR = data['wheelOnRumbleRR'].to_numpy()
#     wheelInPuddleDepthFL = data['wheelInPuddleDepthFL'].to_numpy()
#     wheelInPuddleDepthFR = data['wheelInPuddleDepthFR'].to_numpy()
#     wheelInPuddleDepthRL = data['wheelInPuddleDepthRL'].to_numpy()
#     wheelInPuddleDepthRR = data['wheelInPuddleDepthRR'].to_numpy()
#     forceFeedbackRumbleFL = data['forceFeedbackRumbleFL'].to_numpy()
#     forceFeedbackRumbleFR = data['forceFeedbackRumbleFR'].to_numpy()
#     forceFeedbackRumbleRL = data['forceFeedbackRumbleRL'].to_numpy()
#     forceFeedbackRumbleRR = data['forceFeedbackRumbleRR'].to_numpy()
#     tireSlipAngleFL = data['tireSlipAngleFL'].to_numpy()
#     tireSlipAngleFR = data['tireSlipAngleFR'].to_numpy()
#     tireSlipAngleRL = data['tireSlipAngleRL'].to_numpy()
#     tireSlipAngleRR = data['tireSlipAngleRR'].to_numpy()
#     tireSlipCombinedFL = data['tireSlipCombinedFL'].to_numpy()
#     tireSlipCombinedFR = data['tireSlipCombinedFR'].to_numpy()
#     tireSlipCombinedRL = data['tireSlipCombinedRL'].to_numpy()
#     tireSlipCombinedRR = data['tireSlipCombinedRR'].to_numpy()
#     suspensionTravelFL = data['suspensionTravelFL'].to_numpy()
#     suspensionTravelFR = data['suspensionTravelFR'].to_numpy()
#     suspensionTravelRL = data['suspensionTravelRL'].to_numpy()
#     suspensionTravelRR = data['suspensionTravelRR'].to_numpy()
#     carID = data['carID'].to_numpy()
#     carPerformanceClass = data['carPerformanceClass'].to_numpy()
#     carPerformanceIndex = data['carPerformanceIndex'].to_numpy()
#     carDrivetrainType = data['carDrivetrainType'].to_numpy()
#     carCylinderCount = data['carCylinderCount'].to_numpy()
#     carPositionX = data['carPositionX'].to_numpy()
#     carPositionY = data['carPositionY'].to_numpy()
#     carPositionZ = data['carPositionZ'].to_numpy()
#     carSpeed = data['carSpeed'].to_numpy()
#     enginePower = data['enginePower'].to_numpy()
#     engineTorque = data['engineTorque'].to_numpy()
#     tireTemperatureFL = data['tireTemperatureFL'].to_numpy()
#     tireTemperatureFR = data['tireTemperatureFR'].to_numpy()
#     tireTemperatureRL = data['tireTemperatureRL'].to_numpy()
#     tireTemperatureRR = data['tireTemperatureRR'].to_numpy()
#     engineBoost = data['engineBoost'].to_numpy()
#     engineFuel = data['engineFuel'].to_numpy()
#     distanceTravelled = data['distanceTravelled'].to_numpy()
#     raceBestLap = data['raceBestLap'].to_numpy()
#     raceLastLap = data['raceLastLap'].to_numpy()
#     raceCurrentLap = data['raceCurrentLap'].to_numpy()
#     raceTime = data['raceTime'].to_numpy()
#     raceLap = data['raceLap'].to_numpy()
#     racePosition = data['racePosition'].to_numpy()
#     inputThrottle = data['inputThrottle'].to_numpy()
#     inputBrake = data['inputBrake'].to_numpy()
#     inputClutch = data['inputClutch'].to_numpy()
#     inputHandbrake = data['inputHandbrake'].to_numpy()
#     inputGear = data['inputGear'].to_numpy()
#     inputSteering = data['inputSteering'].to_numpy()
#     normalizedDrivingLine = data['normalizedDrivingLine'].to_numpy()
#     normalizedAIBrakeDifference = data['normalizedAIBrakeDifference'].to_numpy()

#     return (
#         inRace, timestamp, engineMaxRPM, engineIdleRPM, engineRPM,
#         carAccelerationX, carAccelerationY, carAccelerationZ,
#         carVelocityX, carVelocityY, carVelocityZ,
#         carAngularVelocityX, carAngularVelocityY, carAngularVelocityZ,
#         carYaw, carPitch, carRoll,
#         suspensionTravelNormalizedFL, suspensionTravelNormalizedFR,
#         suspensionTravelNormalizedRL, suspensionTravelNormalizedRR,
#         tireSlipRatioFL, tireSlipRatioFR, tireSlipRatioRL, tireSlipRatioRR,
#         wheelRotationSpeedFL, wheelRotationSpeedFR, wheelRotationSpeedRL,
#         wheelRotationSpeedRR, wheelOnRumbleFL, wheelOnRumbleFR, wheelOnRumbleRL,
#         wheelOnRumbleRR, wheelInPuddleDepthFL, wheelInPuddleDepthFR,
#         wheelInPuddleDepthRL, wheelInPuddleDepthRR, forceFeedbackRumbleFL,
#         forceFeedbackRumbleFR, forceFeedbackRumbleRL, forceFeedbackRumbleRR,
#         tireSlipAngleFL, tireSlipAngleFR, tireSlipAngleRL, tireSlipAngleRR,
#         tireSlipCombinedFL, tireSlipCombinedFR, tireSlipCombinedRL,
#         tireSlipCombinedRR, suspensionTravelFL, suspensionTravelFR,
#         suspensionTravelRL, suspensionTravelRR, carID, carPerformanceClass,
#         carPerformanceIndex, carDrivetrainType, carCylinderCount,
#         carPositionX, carPositionY, carPositionZ, carSpeed, enginePower,
#         engineTorque, tireTemperatureFL, tireTemperatureFR, tireTemperatureRL,
#         tireTemperatureRR, engineBoost, engineFuel, distanceTravelled,
#         raceBestLap, raceLastLap, raceCurrentLap, raceTime, raceLap,
#         racePosition, inputThrottle, inputBrake, inputClutch, inputHandbrake,
#         inputGear, inputSteering, normalizedDrivingLine,
#         normalizedAIBrakeDifference
#     )

# def plot_xy_terrain(x_values, y_values, z_values):
#     plt.style.use('dark_background')
#     plt.scatter(x_values, y_values, c=z_values, cmap='RdYlGn', marker='o', label='Data')
#     cbar = plt.colorbar()
#     cbar.set_label('Z Values')
#     plt.xlabel('X Values')
#     plt.ylabel('Y Values')
#     plt.title('Terrain')
#     plt.show()

def plot_terrain(fileName):
    data = extract_csv(get_csv_data_local('creampie.csv'))
    x_values = data['carPositionX']
    y_values = data['carPositionY']
    z_values = data['carPositionZ']
    plt.style.use('dark_background')
    plt.scatter(x_values, y_values, c=z_values, cmap='RdYlGn', marker='o', label='Data')
    cbar = plt.colorbar()
    cbar.set_label('Z Values')
    plt.xlabel('X Values')
    plt.ylabel('Y Values')
    plt.title('Terrain')
    plt.show()

csv_data = get_csv_data_local('creampie.csv')
csv = extract_csv(csv_data)
plot_terrain('creampie.csv')
