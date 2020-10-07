import numpy as np
import pandas as pd
import glob
import csv

# Set path to files
path = '/Users/OwenO/Downloads/train'
# This bit will allow us to cycle through all files in the folder
all_files = glob.glob(path + "/*.csv")

# Create an empty list
li = []
# Read in each file from the folder and add them to the list
# WARNING This may not read in the CSVs in the order they were in in the folder
for filename in all_files:
    df = pd.read_csv(filename, header=None, skiprows=7, sep='\n', skip_blank_lines=False, quoting=csv.QUOTE_NONE)
    df = df[0].str.split(',', expand=True)
    li.append(df)

colnams = ['Time', 'BT', 'Acc1', 'Acc2', 'Acc3', 'Gyr1', 'Gyr2', 'Gyr3',
           'Att1', 'Att2', 'Att3', 'Gra1', 'Gra2', 'Gra3',
           'Mag1', 'Mag2', 'Mag3', 'Mag4', 'Alt1', 'Alt2',
           'Hea1', 'Hea2', 'Hea3', 'Hea4', 'Hea5', 'Hea6']

data = pd.DataFrame(columns=colnams)

# Arrange the data into a nice data frame which is easier to analyse
for i in range(len(li[0])):
    data.loc[i, 'Time'] = li[0].iloc[i, 0]
    if li[0].iloc[i, 1] == 'Bluetooth':
        data.loc[i, 'BT'] = li[0].iloc[i, 2]
        for k in reversed(range(i)):
            if li[0].iloc[k, 1] == 'Accelerometer':
                if li[0].iloc[k, 2] == li[0].iloc[k, 2]:
                    data.loc[i, 'Acc1'] = li[0].iloc[k, 2]
                    data.loc[i, 'Acc2'] = li[0].iloc[k, 3]
                    data.loc[i, 'Acc3'] = li[0].iloc[k, 4]
                    break
        for k in reversed(range(i)):
            if li[0].iloc[k, 1] == 'Gyroscope':
                if li[0].iloc[k, 2] == li[0].iloc[k, 2]:
                    data.loc[i, 'Gyr1'] = li[0].iloc[k, 2]
                    data.loc[i, 'Gyr2'] = li[0].iloc[k, 3]
                    data.loc[i, 'Gyr3'] = li[0].iloc[k, 4]
                    break
        for k in reversed(range(i)):
            if li[0].iloc[k, 1] == 'Attitude':
                if li[0].iloc[k, 2] == li[0].iloc[k, 2]:
                    data.loc[i, 'Att1'] = li[0].iloc[k, 2]
                    data.loc[i, 'Att2'] = li[0].iloc[k, 3]
                    data.loc[i, 'Att3'] = li[0].iloc[k, 4]
                    break
        for k in reversed(range(i)):
            if li[0].iloc[k, 1] == 'Gravity':
                if li[0].iloc[k, 2] == li[0].iloc[k, 2]:
                    data.loc[i, 'Gra1'] = li[0].iloc[k, 2]
                    data.loc[i, 'Gra2'] = li[0].iloc[k, 3]
                    data.loc[i, 'Gra3'] = li[0].iloc[k, 4]
                    break
        for k in reversed(range(i)):
            if li[0].iloc[k, 1] == 'Magnetic-field':
                if li[0].iloc[k, 2] == li[0].iloc[k, 2]:
                    data.loc[i, 'Mag1'] = li[0].iloc[k, 2]
                    data.loc[i, 'Mag2'] = li[0].iloc[k, 3]
                    data.loc[i, 'Mag3'] = li[0].iloc[k, 4]
                    data.loc[i, 'Mag4'] = li[0].iloc[k, 5]
                    break
        for k in reversed(range(i)):
            if li[0].iloc[k, 1] == 'Altitude':
                if li[0].iloc[k, 2] == li[0].iloc[k, 2]:
                    data.loc[i, 'Alt1'] = li[0].iloc[k, 2]
                    data.loc[i, 'Alt2'] = li[0].iloc[k, 3]
                    break
        for k in reversed(range(i)):
            if li[0].iloc[k, 1] == 'Heading':
                if li[0].iloc[k, 2] == li[0].iloc[k, 2]:
                    data.loc[i, 'Hea1'] = li[0].iloc[k, 2]
                    data.loc[i, 'Hea2'] = li[0].iloc[k, 3]
                    data.loc[i, 'Hea3'] = li[0].iloc[k, 4]
                    data.loc[i, 'Hea4'] = li[0].iloc[k, 5]
                    data.loc[i, 'Hea5'] = li[0].iloc[k, 6]
                    data.loc[i, 'Hea6'] = li[0].iloc[k, 7]
                    break
    elif li[0].iloc[i, 1] == 'Accelerometer':
        data.loc[i, 'Acc1'] = li[0].iloc[i, 2]
        data.loc[i, 'Acc2'] = li[0].iloc[i, 3]
        data.loc[i, 'Acc3'] = li[0].iloc[i, 4]
        for k in reversed(range(i)):
            if li[0].iloc[k, 1] == 'Bluetooth':
                if li[0].iloc[k, 2] == li[0].iloc[k, 2]:
                    data.loc[i, 'BT'] = li[0].iloc[k, 2]
                    break
        for k in reversed(range(i)):
            if li[0].iloc[k, 1] == 'Gyroscope':
                if li[0].iloc[k, 2] == li[0].iloc[k, 2]:
                    data.loc[i, 'Gyr1'] = li[0].iloc[k, 2]
                    data.loc[i, 'Gyr2'] = li[0].iloc[k, 3]
                    data.loc[i, 'Gyr3'] = li[0].iloc[k, 4]
                    break
        for k in reversed(range(i)):
            if li[0].iloc[k, 1] == 'Attitude':
                if li[0].iloc[k, 2] == li[0].iloc[k, 2]:
                    data.loc[i, 'Att1'] = li[0].iloc[k, 2]
                    data.loc[i, 'Att2'] = li[0].iloc[k, 3]
                    data.loc[i, 'Att3'] = li[0].iloc[k, 4]
                    break
        for k in reversed(range(i)):
            if li[0].iloc[k, 1] == 'Gravity':
                if li[0].iloc[k, 2] == li[0].iloc[k, 2]:
                    data.loc[i, 'Gra1'] = li[0].iloc[k, 2]
                    data.loc[i, 'Gra2'] = li[0].iloc[k, 3]
                    data.loc[i, 'Gra3'] = li[0].iloc[k, 4]
                    break
        for k in reversed(range(i)):
            if li[0].iloc[k, 1] == 'Magnetic-field':
                if li[0].iloc[k, 2] == li[0].iloc[k, 2]:
                    data.loc[i, 'Mag1'] = li[0].iloc[k, 2]
                    data.loc[i, 'Mag2'] = li[0].iloc[k, 3]
                    data.loc[i, 'Mag3'] = li[0].iloc[k, 4]
                    data.loc[i, 'Mag4'] = li[0].iloc[k, 5]
                    break
        for k in reversed(range(i)):
            if li[0].iloc[k, 1] == 'Altitude':
                if li[0].iloc[k, 2] == li[0].iloc[k, 2]:
                    data.loc[i, 'Alt1'] = li[0].iloc[k, 2]
                    data.loc[i, 'Alt2'] = li[0].iloc[k, 3]
                    break
        for k in reversed(range(i)):
            if li[0].iloc[k, 1] == 'Heading':
                if li[0].iloc[k, 2] == li[0].iloc[k, 2]:
                    data.loc[i, 'Hea1'] = li[0].iloc[k, 2]
                    data.loc[i, 'Hea2'] = li[0].iloc[k, 3]
                    data.loc[i, 'Hea3'] = li[0].iloc[k, 4]
                    data.loc[i, 'Hea4'] = li[0].iloc[k, 5]
                    data.loc[i, 'Hea5'] = li[0].iloc[k, 6]
                    data.loc[i, 'Hea6'] = li[0].iloc[k, 7]
                    break
    elif li[0].iloc[i, 1] == 'Gyroscope':
        data.loc[i, 'Gyr1'] = li[0].iloc[i, 2]
        data.loc[i, 'Gyr2'] = li[0].iloc[i, 3]
        data.loc[i, 'Gyr3'] = li[0].iloc[i, 4]
        for k in reversed(range(i)):
            if li[0].iloc[k, 1] == 'Bluetooth':
                if li[0].iloc[k, 2] == li[0].iloc[k, 2]:
                    data.loc[i, 'BT'] = li[0].iloc[k, 2]
                    break
        for k in reversed(range(i)):
            if li[0].iloc[k, 1] == 'Accelerometer':
                if li[0].iloc[k, 2] == li[0].iloc[k, 2]:
                    data.loc[i, 'Acc1'] = li[0].iloc[k, 2]
                    data.loc[i, 'Acc2'] = li[0].iloc[k, 3]
                    data.loc[i, 'Acc3'] = li[0].iloc[k, 4]
                    break
        for k in reversed(range(i)):
            if li[0].iloc[k, 1] == 'Attitude':
                if li[0].iloc[k, 2] == li[0].iloc[k, 2]:
                    data.loc[i, 'Att1'] = li[0].iloc[k, 2]
                    data.loc[i, 'Att2'] = li[0].iloc[k, 3]
                    data.loc[i, 'Att3'] = li[0].iloc[k, 4]
                    break
        for k in reversed(range(i)):
            if li[0].iloc[k, 1] == 'Gravity':
                if li[0].iloc[k, 2] == li[0].iloc[k, 2]:
                    data.loc[i, 'Gra1'] = li[0].iloc[k, 2]
                    data.loc[i, 'Gra2'] = li[0].iloc[k, 3]
                    data.loc[i, 'Gra3'] = li[0].iloc[k, 4]
                    break
        for k in reversed(range(i)):
            if li[0].iloc[k, 1] == 'Magnetic-field':
                if li[0].iloc[k, 2] == li[0].iloc[k, 2]:
                    data.loc[i, 'Mag1'] = li[0].iloc[k, 2]
                    data.loc[i, 'Mag2'] = li[0].iloc[k, 3]
                    data.loc[i, 'Mag3'] = li[0].iloc[k, 4]
                    data.loc[i, 'Mag4'] = li[0].iloc[k, 5]
                    break
        for k in reversed(range(i)):
            if li[0].iloc[k, 1] == 'Altitude':
                if li[0].iloc[k, 2] == li[0].iloc[k, 2]:
                    data.loc[i, 'Alt1'] = li[0].iloc[k, 2]
                    data.loc[i, 'Alt2'] = li[0].iloc[k, 3]
                    break
        for k in reversed(range(i)):
            if li[0].iloc[k, 1] == 'Heading':
                if li[0].iloc[k, 2] == li[0].iloc[k, 2]:
                    data.loc[i, 'Hea1'] = li[0].iloc[k, 2]
                    data.loc[i, 'Hea2'] = li[0].iloc[k, 3]
                    data.loc[i, 'Hea3'] = li[0].iloc[k, 4]
                    data.loc[i, 'Hea4'] = li[0].iloc[k, 5]
                    data.loc[i, 'Hea5'] = li[0].iloc[k, 6]
                    data.loc[i, 'Hea6'] = li[0].iloc[k, 7]
                    break
    elif li[0].iloc[i, 1] == 'Attitude':
        data.loc[i, 'Att1'] = li[0].iloc[i, 2]
        data.loc[i, 'Att2'] = li[0].iloc[i, 3]
        data.loc[i, 'Att3'] = li[0].iloc[i, 4]
        for k in reversed(range(i)):
            if li[0].iloc[k, 1] == 'Bluetooth':
                if li[0].iloc[k, 2] == li[0].iloc[k, 2]:
                    data.loc[i, 'BT'] = li[0].iloc[k, 2]
                    break
        for k in reversed(range(i)):
            if li[0].iloc[k, 1] == 'Accelerometer':
                if li[0].iloc[k, 2] == li[0].iloc[k, 2]:
                    data.loc[i, 'Acc1'] = li[0].iloc[k, 2]
                    data.loc[i, 'Acc2'] = li[0].iloc[k, 3]
                    data.loc[i, 'Acc3'] = li[0].iloc[k, 4]
                    break
        for k in reversed(range(i)):
            if li[0].iloc[k, 1] == 'Gyroscope':
                if li[0].iloc[k, 2] == li[0].iloc[k, 2]:
                    data.loc[i, 'Gyr1'] = li[0].iloc[k, 2]
                    data.loc[i, 'Gyr2'] = li[0].iloc[k, 3]
                    data.loc[i, 'Gyr3'] = li[0].iloc[k, 4]
                    break
        for k in reversed(range(i)):
            if li[0].iloc[k, 1] == 'Gravity':
                if li[0].iloc[k, 2] == li[0].iloc[k, 2]:
                    data.loc[i, 'Gra1'] = li[0].iloc[k, 2]
                    data.loc[i, 'Gra2'] = li[0].iloc[k, 3]
                    data.loc[i, 'Gra3'] = li[0].iloc[k, 4]
                    break
        for k in reversed(range(i)):
            if li[0].iloc[k, 1] == 'Magnetic-field':
                if li[0].iloc[k, 2] == li[0].iloc[k, 2]:
                    data.loc[i, 'Mag1'] = li[0].iloc[k, 2]
                    data.loc[i, 'Mag2'] = li[0].iloc[k, 3]
                    data.loc[i, 'Mag3'] = li[0].iloc[k, 4]
                    data.loc[i, 'Mag4'] = li[0].iloc[k, 5]
                    break
        for k in reversed(range(i)):
            if li[0].iloc[k, 1] == 'Altitude':
                if li[0].iloc[k, 2] == li[0].iloc[k, 2]:
                    data.loc[i, 'Alt1'] = li[0].iloc[k, 2]
                    data.loc[i, 'Alt2'] = li[0].iloc[k, 3]
                    break
        for k in reversed(range(i)):
            if li[0].iloc[k, 1] == 'Heading':
                if li[0].iloc[k, 2] == li[0].iloc[k, 2]:
                    data.loc[i, 'Hea1'] = li[0].iloc[k, 2]
                    data.loc[i, 'Hea2'] = li[0].iloc[k, 3]
                    data.loc[i, 'Hea3'] = li[0].iloc[k, 4]
                    data.loc[i, 'Hea4'] = li[0].iloc[k, 5]
                    data.loc[i, 'Hea5'] = li[0].iloc[k, 6]
                    data.loc[i, 'Hea6'] = li[0].iloc[k, 7]
                    break
    elif li[0].iloc[i, 1] == 'Gravity':
        data.loc[i, 'Gra1'] = li[0].iloc[i, 2]
        data.loc[i, 'Gra2'] = li[0].iloc[i, 3]
        data.loc[i, 'Gra3'] = li[0].iloc[i, 4]
        for k in reversed(range(i)):
            if li[0].iloc[k, 1] == 'Bluetooth':
                if li[0].iloc[k, 2] == li[0].iloc[k, 2]:
                    data.loc[i, 'BT'] = li[0].iloc[k, 2]
                    break
        for k in reversed(range(i)):
            if li[0].iloc[k, 1] == 'Accelerometer':
                if li[0].iloc[k, 2] == li[0].iloc[k, 2]:
                    data.loc[i, 'Acc1'] = li[0].iloc[k, 2]
                    data.loc[i, 'Acc2'] = li[0].iloc[k, 3]
                    data.loc[i, 'Acc3'] = li[0].iloc[k, 4]
                    break
        for k in reversed(range(i)):
            if li[0].iloc[k, 1] == 'Gyroscope':
                if li[0].iloc[k, 2] == li[0].iloc[k, 2]:
                    data.loc[i, 'Gyr1'] = li[0].iloc[k, 2]
                    data.loc[i, 'Gyr2'] = li[0].iloc[k, 3]
                    data.loc[i, 'Gyr3'] = li[0].iloc[k, 4]
                    break
        for k in reversed(range(i)):
            if li[0].iloc[k, 1] == 'Attitude':
                if li[0].iloc[k, 2] == li[0].iloc[k, 2]:
                    data.loc[i, 'Att1'] = li[0].iloc[k, 2]
                    data.loc[i, 'Att2'] = li[0].iloc[k, 3]
                    data.loc[i, 'Att3'] = li[0].iloc[k, 4]
                    break
        for k in reversed(range(i)):
            if li[0].iloc[k, 1] == 'Magnetic-field':
                if li[0].iloc[k, 2] == li[0].iloc[k, 2]:
                    data.loc[i, 'Mag1'] = li[0].iloc[k, 2]
                    data.loc[i, 'Mag2'] = li[0].iloc[k, 3]
                    data.loc[i, 'Mag3'] = li[0].iloc[k, 4]
                    data.loc[i, 'Mag4'] = li[0].iloc[k, 5]
                    break
        for k in reversed(range(i)):
            if li[0].iloc[k, 1] == 'Altitude':
                if li[0].iloc[k, 2] == li[0].iloc[k, 2]:
                    data.loc[i, 'Alt1'] = li[0].iloc[k, 2]
                    data.loc[i, 'Alt2'] = li[0].iloc[k, 3]
                    break
        for k in reversed(range(i)):
            if li[0].iloc[k, 1] == 'Heading':
                if li[0].iloc[k, 2] == li[0].iloc[k, 2]:
                    data.loc[i, 'Hea1'] = li[0].iloc[k, 2]
                    data.loc[i, 'Hea2'] = li[0].iloc[k, 3]
                    data.loc[i, 'Hea3'] = li[0].iloc[k, 4]
                    data.loc[i, 'Hea4'] = li[0].iloc[k, 5]
                    data.loc[i, 'Hea5'] = li[0].iloc[k, 6]
                    data.loc[i, 'Hea6'] = li[0].iloc[k, 7]
                    break
    elif li[0].iloc[i, 1] == 'Magnetic-field':
        data.loc[i, 'Mag1'] = li[0].iloc[i, 2]
        data.loc[i, 'Mag2'] = li[0].iloc[i, 3]
        data.loc[i, 'Mag3'] = li[0].iloc[i, 4]
        data.loc[i, 'Mag4'] = li[0].iloc[i, 5]
        for k in reversed(range(i)):
            if li[0].iloc[k, 1] == 'Bluetooth':
                if li[0].iloc[k, 2] == li[0].iloc[k, 2]:
                    data.loc[i, 'BT'] = li[0].iloc[k, 2]
                    break
        for k in reversed(range(i)):
            if li[0].iloc[k, 1] == 'Accelerometer':
                if li[0].iloc[k, 2] == li[0].iloc[k, 2]:
                    data.loc[i, 'Acc1'] = li[0].iloc[k, 2]
                    data.loc[i, 'Acc2'] = li[0].iloc[k, 3]
                    data.loc[i, 'Acc3'] = li[0].iloc[k, 4]
                    break
        for k in reversed(range(i)):
            if li[0].iloc[k, 1] == 'Gyroscope':
                if li[0].iloc[k, 2] == li[0].iloc[k, 2]:
                    data.loc[i, 'Gyr1'] = li[0].iloc[k, 2]
                    data.loc[i, 'Gyr2'] = li[0].iloc[k, 3]
                    data.loc[i, 'Gyr3'] = li[0].iloc[k, 4]
                    break
        for k in reversed(range(i)):
            if li[0].iloc[k, 1] == 'Attitude':
                if li[0].iloc[k, 2] == li[0].iloc[k, 2]:
                    data.loc[i, 'Att1'] = li[0].iloc[k, 2]
                    data.loc[i, 'Att2'] = li[0].iloc[k, 3]
                    data.loc[i, 'Att3'] = li[0].iloc[k, 4]
                    break
        for k in reversed(range(i)):
            if li[0].iloc[k, 1] == 'Gravity':
                if li[0].iloc[k, 2] == li[0].iloc[k, 2]:
                    data.loc[i, 'Gra1'] = li[0].iloc[k, 2]
                    data.loc[i, 'Gra2'] = li[0].iloc[k, 3]
                    data.loc[i, 'Gra3'] = li[0].iloc[k, 4]
                    break
        for k in reversed(range(i)):
            if li[0].iloc[k, 1] == 'Altitude':
                if li[0].iloc[k, 2] == li[0].iloc[k, 2]:
                    data.loc[i, 'Alt1'] = li[0].iloc[k, 2]
                    data.loc[i, 'Alt2'] = li[0].iloc[k, 3]
                    break
        for k in reversed(range(i)):
            if li[0].iloc[k, 1] == 'Heading':
                if li[0].iloc[k, 2] == li[0].iloc[k, 2]:
                    data.loc[i, 'Hea1'] = li[0].iloc[k, 2]
                    data.loc[i, 'Hea2'] = li[0].iloc[k, 3]
                    data.loc[i, 'Hea3'] = li[0].iloc[k, 4]
                    data.loc[i, 'Hea4'] = li[0].iloc[k, 5]
                    data.loc[i, 'Hea5'] = li[0].iloc[k, 6]
                    data.loc[i, 'Hea6'] = li[0].iloc[k, 7]
                    break
    elif li[0].iloc[i, 1] == 'Altitude':
        data.loc[i, 'Alt1'] = li[0].iloc[i, 2]
        data.loc[i, 'Alt2'] = li[0].iloc[i, 3]
        for k in reversed(range(i)):
            if li[0].iloc[k, 1] == 'Bluetooth':
                if li[0].iloc[k, 2] == li[0].iloc[k, 2]:
                    data.loc[i, 'BT'] = li[0].iloc[k, 2]
                    break
        for k in reversed(range(i)):
            if li[0].iloc[k, 1] == 'Accelerometer':
                if li[0].iloc[k, 2] == li[0].iloc[k, 2]:
                    data.loc[i, 'Acc1'] = li[0].iloc[k, 2]
                    data.loc[i, 'Acc2'] = li[0].iloc[k, 3]
                    data.loc[i, 'Acc3'] = li[0].iloc[k, 4]
                    break
        for k in reversed(range(i)):
            if li[0].iloc[k, 1] == 'Gyroscope':
                if li[0].iloc[k, 2] == li[0].iloc[k, 2]:
                    data.loc[i, 'Gyr1'] = li[0].iloc[k, 2]
                    data.loc[i, 'Gyr2'] = li[0].iloc[k, 3]
                    data.loc[i, 'Gyr3'] = li[0].iloc[k, 4]
                    break
        for k in reversed(range(i)):
            if li[0].iloc[k, 1] == 'Attitude':
                if li[0].iloc[k, 2] == li[0].iloc[k, 2]:
                    data.loc[i, 'Att1'] = li[0].iloc[k, 2]
                    data.loc[i, 'Att2'] = li[0].iloc[k, 3]
                    data.loc[i, 'Att3'] = li[0].iloc[k, 4]
                    break
        for k in reversed(range(i)):
            if li[0].iloc[k, 1] == 'Gravity':
                if li[0].iloc[k, 2] == li[0].iloc[k, 2]:
                    data.loc[i, 'Gra1'] = li[0].iloc[k, 2]
                    data.loc[i, 'Gra2'] = li[0].iloc[k, 3]
                    data.loc[i, 'Gra3'] = li[0].iloc[k, 4]
                    break
        for k in reversed(range(i)):
            if li[0].iloc[k, 1] == 'Magnetic-field':
                if li[0].iloc[k, 2] == li[0].iloc[k, 2]:
                    data.loc[i, 'Mag1'] = li[0].iloc[k, 2]
                    data.loc[i, 'Mag2'] = li[0].iloc[k, 3]
                    data.loc[i, 'Mag3'] = li[0].iloc[k, 4]
                    data.loc[i, 'Mag4'] = li[0].iloc[k, 5]
                    break
        for k in reversed(range(i)):
            if li[0].iloc[k, 1] == 'Heading':
                if li[0].iloc[k, 2] == li[0].iloc[k, 2]:
                    data.loc[i, 'Hea1'] = li[0].iloc[k, 2]
                    data.loc[i, 'Hea2'] = li[0].iloc[k, 3]
                    data.loc[i, 'Hea3'] = li[0].iloc[k, 4]
                    data.loc[i, 'Hea4'] = li[0].iloc[k, 5]
                    data.loc[i, 'Hea5'] = li[0].iloc[k, 6]
                    data.loc[i, 'Hea6'] = li[0].iloc[k, 7]
                    break
    else:
        data.loc[i, 'Hea1'] = li[0].iloc[i, 2]
        data.loc[i, 'Hea2'] = li[0].iloc[i, 3]
        data.loc[i, 'Hea3'] = li[0].iloc[i, 4]
        data.loc[i, 'Hea4'] = li[0].iloc[i, 5]
        data.loc[i, 'Hea5'] = li[0].iloc[i, 6]
        data.loc[i, 'Hea6'] = li[0].iloc[i, 7]
        for k in reversed(range(i)):
            if li[0].iloc[k, 1] == 'Bluetooth':
                if li[0].iloc[k, 2] == li[0].iloc[k, 2]:
                    data.loc[i, 'BT'] = li[0].iloc[k, 2]
                    break
        for k in reversed(range(i)):
            if li[0].iloc[k, 1] == 'Accelerometer':
                if li[0].iloc[k, 2] == li[0].iloc[k, 2]:
                    data.loc[i, 'Acc1'] = li[0].iloc[k, 2]
                    data.loc[i, 'Acc2'] = li[0].iloc[k, 3]
                    data.loc[i, 'Acc3'] = li[0].iloc[k, 4]
                    break
        for k in reversed(range(i)):
            if li[0].iloc[k, 1] == 'Gyroscope':
                if li[0].iloc[k, 2] == li[0].iloc[k, 2]:
                    data.loc[i, 'Gyr1'] = li[0].iloc[k, 2]
                    data.loc[i, 'Gyr2'] = li[0].iloc[k, 3]
                    data.loc[i, 'Gyr3'] = li[0].iloc[k, 4]
                    break
        for k in reversed(range(i)):
            if li[0].iloc[k, 1] == 'Attitude':
                if li[0].iloc[k, 2] == li[0].iloc[k, 2]:
                    data.loc[i, 'Att1'] = li[0].iloc[k, 2]
                    data.loc[i, 'Att2'] = li[0].iloc[k, 3]
                    data.loc[i, 'Att3'] = li[0].iloc[k, 4]
                    break
        for k in reversed(range(i)):
            if li[0].iloc[k, 1] == 'Gravity':
                if li[0].iloc[k, 2] == li[0].iloc[k, 2]:
                    data.loc[i, 'Gra1'] = li[0].iloc[k, 2]
                    data.loc[i, 'Gra2'] = li[0].iloc[k, 3]
                    data.loc[i, 'Gra3'] = li[0].iloc[k, 4]
                    break
        for k in reversed(range(i)):
            if li[0].iloc[k, 1] == 'Magnetic-field':
                if li[0].iloc[k, 2] == li[0].iloc[k, 2]:
                    data.loc[i, 'Mag1'] = li[0].iloc[k, 2]
                    data.loc[i, 'Mag2'] = li[0].iloc[k, 3]
                    data.loc[i, 'Mag3'] = li[0].iloc[k, 4]
                    data.loc[i, 'Mag4'] = li[0].iloc[k, 5]
                    break
        for k in reversed(range(i)):
            if li[0].iloc[k, 1] == 'Altitude':
                if li[0].iloc[k, 2] == li[0].iloc[k, 2]:
                    data.loc[i, 'Alt1'] = li[0].iloc[k, 2]
                    data.loc[i, 'Alt2'] = li[0].iloc[k, 3]
                    break


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)

print(data)
