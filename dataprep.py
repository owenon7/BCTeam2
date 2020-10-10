import pandas as pd
import glob
import csv

# Set path to files
path = '/Users/OwenO/Downloads/train'
# This bit will allow us to cycle through all files in the folder
all_files = glob.glob(path + "/*.csv")

# Read in each file from the folder and add them to the list
# WARNING This may not read in the CSVs in the order they were in in the folder
for filename in all_files:
    df = pd.read_csv(filename, header=None, skiprows=7, sep='\n',
                     skip_blank_lines=False, quoting=csv.QUOTE_NONE)
    df = df[0].str.split(',', expand=True)

    cdata = pd.DataFrame(columns=['Time', 'BT', 'Acc1', 'Acc2', 'Acc3', 'Gyr1', 'Gyr2', 'Gyr3',
                                  'Att1', 'Att2', 'Att3', 'Gra1', 'Gra2', 'Gra3',
                                  'Mag1', 'Mag2', 'Mag3', 'Mag4', 'Alt1', 'Alt2',
                                  'Hea1', 'Hea2', 'Hea3', 'Hea4', 'Hea5', 'Hea6'])
    for i in range(len(df)):
        cdata.loc[i, 'Time'] = df.iloc[i, 0]
        if df.iloc[i, 1] == 'Bluetooth':
            cdata.loc[i, 'BT'] = df.iloc[i, 2]
        elif df.iloc[i, 1] == 'Accelerometer':
            cdata.loc[i, 'Acc1'] = df.iloc[i, 2]
            cdata.loc[i, 'Acc2'] = df.iloc[i, 3]
            cdata.loc[i, 'Acc3'] = df.iloc[i, 4]
        elif df.iloc[i, 1] == 'Gyroscope':
            cdata.loc[i, 'Gyr1'] = df.iloc[i, 2]
            cdata.loc[i, 'Gyr2'] = df.iloc[i, 3]
            cdata.loc[i, 'Gyr3'] = df.iloc[i, 4]
        elif df.iloc[i, 1] == 'Attitude':
            cdata.loc[i, 'Att1'] = df.iloc[i, 2]
            cdata.loc[i, 'Att2'] = df.iloc[i, 3]
            cdata.loc[i, 'Att3'] = df.iloc[i, 4]
        elif df.iloc[i, 1] == 'Gravity':
            cdata.loc[i, 'Gra1'] = df.iloc[i, 2]
            cdata.loc[i, 'Gra2'] = df.iloc[i, 3]
            cdata.loc[i, 'Gra3'] = df.iloc[i, 4]
        elif df.iloc[i, 1] == 'Magnetic-field':
            cdata.loc[i, 'Mag1'] = df.iloc[i, 2]
            cdata.loc[i, 'Mag2'] = df.iloc[i, 3]
            cdata.loc[i, 'Mag3'] = df.iloc[i, 4]
            cdata.loc[i, 'Mag4'] = df.iloc[i, 5]
        elif df.iloc[i, 1] == 'Altitude':
            cdata.loc[i, 'Alt1'] = df.iloc[i, 2]
            cdata.loc[i, 'Alt2'] = df.iloc[i, 3]
        elif df.iloc[i, 1] == 'Heading':
            cdata.loc[i, 'Hea1'] = df.iloc[i, 2]
            cdata.loc[i, 'Hea2'] = df.iloc[i, 3]
            cdata.loc[i, 'Hea3'] = df.iloc[i, 4]
            cdata.loc[i, 'Hea4'] = df.iloc[i, 5]
            cdata.loc[i, 'Hea5'] = df.iloc[i, 6]
            cdata.loc[i, 'Hea6'] = df.iloc[i, 7]

    cdata = cdata.fillna(method='ffill')
    cdata = cdata.fillna(method='bfill')

    cdata.to_csv(filename, index=False)
