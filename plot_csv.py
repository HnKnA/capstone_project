import pandas as pd
import matplotlib.pyplot as plt

# Replace 'your_csv_file.csv' with the path to your CSV file
csv_file_path = 'csv/noise/C/C_17.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Plotting each column
plt.figure(figsize=(15, 10))  # Adjust the size as per your preference

# Loop through the columns and plot
for column in df.columns:
    plt.plot(df[column], label=column)

# Add legend, title, labels, and grid
plt.legend()
plt.title('Data from CSV file')
plt.xlabel('Index')
plt.ylabel('Values')
plt.grid(True)

# Show the plot
plt.show()
