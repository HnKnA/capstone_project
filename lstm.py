import tensorflow as tf
import numpy as np
import pandas as pd
import tensorflow as tf


GESTURES = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
    "K", "L","M", "N", "O", "P", "Q", "R", "S", "T",
    "U", "V", "W", "X", "Y", "Z", "idle"
]
column_mapping = {
    'column_0': 'ax',
    'column_1': 'ay',
    'column_2': 'az',
    'column_3': 'gx',
    'column_4': 'gy',
    'column_5': 'gz',
}
labels = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
    "K", "L","M", "N", "O", "P", "Q", "R", "S", "T",
    "U", "V", "W", "X", "Y", "Z", "idle"
]

predict_aray = []

g = 9.80665
#from csv/official/A_1.csv import to df
model = tf.keras.models.load_model('lstm_raw')
for label in labels:
    correct = 0
    file_number = 0
    for i in range(0,20):
        file_number = file_number + 1
        file_name = f'./csv/noise/{label}/{label}_{i}.csv'   
        # print(f"Reading file {file_name}")
        df = pd.read_csv(file_name)
        df = df.rename(columns=column_mapping)
        df['ax'] = (df['ax'] / 8*g) 
        df['ay'] = (df['ay'] / 8*g)
        df['az'] = (df['az'] / 8*g) 
        df['gx'] = (df['gx'] / 1000) 
        df['gy'] = (df['gy'] / 1000) 
        df['gz'] = (df['gz'] / 1000) 
        zeros_to_add = 85 - len(df)
        # print(zeros_to_add)
        if zeros_to_add > 0:
            zeros_df = pd.DataFrame(0, index=np.arange(zeros_to_add), columns=df.columns)
            df = df._append(zeros_df, ignore_index=True)
        df = df.iloc[15:85].astype('float').to_numpy()
        reshaped = df.reshape(1,70,6)
        prediction = model.predict(reshaped)
        prediction = prediction * 1000 *1000
        # print(GESTURES[np.argmax(prediction)])
        # print(prediction)
        if GESTURES[np.argmax(prediction)]==label:
            correct += 1
    print(f"Accuracy for {label}: {correct}/{file_number}")