import os

label = "L"

# Define the directory where the files are located
directory = f'./csv/unofficial/{label}'

# Define the starting and ending numbers for the original and new filenames
start_original = 0
end_original = 19
start_new = 100

# Iterate over the range of files and rename each one
for i in range(start_original, end_original + 1):
    # Generate the old and new file names
    old_name = f"{label}_{i}.csv"
    new_name = f"{label}_{start_new + i - start_original}.csv"
    
    # Generate the full path for the old and new file names
    old_file_path = os.path.join(directory, old_name)
    new_file_path = os.path.join(directory, new_name)
    
    # Rename the file
    os.rename(old_file_path, new_file_path)
    print(f"Renamed {old_file_path} to {new_file_path}")
