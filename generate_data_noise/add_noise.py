import pandas as pd
import numpy as np
import os

labels = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
    "K", "L","M", "N", "O", "P", "Q", "R", "S", "T",
    "U", "V", "W", "X", "Y", "Z", "idle"
]

for label in labels:

    for i in range(0,20):
        file_name = f'./csv/unofficial/{label}/{label}_{i}.csv'   
        data = pd.read_csv(file_name)
        
        # Splitting the dataframe into two parts
        accel_columns = data.iloc[:, :3]
        gyro_columns = data.iloc[:, -3:]

        # Adding noise to the first three columns
        noisy_accel_columns = accel_columns.apply(lambda x: x + np.random.uniform(-1, 1, size=len(x)))

        # Adding noise to the last three columns
        noisy_gyro_columns = gyro_columns.apply(lambda x: x + np.random.uniform(-10, 10, size=len(x)))

        # Concatenating the modified columns back together
        noisy_data = pd.concat([noisy_accel_columns, noisy_gyro_columns], axis=1)
        
        if not os.path.exists(f"./csv/noise/{label}"):
            os.makedirs(f"./csv/noise/{label}")

        # Step 3: Save the modified data to a new file
        modified_data_file_path = f'./csv/noise/{label}/{label}_{i}.csv'   
        noisy_data.to_csv(modified_data_file_path, index=False)
