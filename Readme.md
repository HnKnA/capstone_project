# Running the IMU Capture and CSV Upload Scripts

To use these scripts, follow these steps:

# Getting Started

This project use the following packages:
`pip install os, time, csv, serial, requests, json, argparse`

# Usage

## CSV Folder
Inofficial: Source data for the main model <br />
Official: Raw original data <br />
Unofficial: Data samples for test <br />
Noise: Data samples after adding noise for test


## CSV Upload Script

Run the `read_to_csv.py` script. This script will read the serial port and write the data to a CSV file. The script will also upload the CSV file to the server.
The scipt takes 3 arguments: port, filename, and official (optional). port is the COM port of the connected devices, filename is the name of the CSV file, and official is a boolean value that determines if the data is official or not if official is true the data will be saved in csv/official and csv/unofficial otherwise. The default value for official is false.

Sample command to run the script with COM3, A.csv and official data:
`python read_to_csv.py COM6 A.csv --official`


## Main model
The main model is in `hgr_test.ipynb`. The currently source data for the model is in csv/inofficial.


## Testing sample
Run the `lstm.py` script. Configure the directory of the sample (official, unofficial, inofficial, noise).


## Rename the csv file
Run the `rename.py` script.


## Plot one csv file
Run the `plot_csv.py` script.
