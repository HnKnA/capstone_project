import os
import numpy as np
import csv
import matplotlib.pyplot as plt

filename = 'Odata.csv'  #name of data file

csv_path = os.path.join("csv/", "official/", filename)

X = np.genfromtxt(csv_path, delimiter=',', skip_header=1) #Original data matrix

n, M = X.shape #row and column of original matrix

#L = int(input('Number of Eigen Values to keep: '))
L = 3
#Number of elements to keep

XX = X.copy()

m = np.mean(X, axis=0) #mean of X

#Subtract the mean from each value of X so that the data does not vary too much when calculating
for i in range(n):
    X[i, :] = X[i, :] - m

#Covariance matrix
Q = np.dot(np.transpose(X.copy()), X) / (n-1)

#Getting Eigen values and Eigen vectors
Eigenval, Eigenvec = np.linalg.eig(Q)


Eval = np.real(Eigenval)

# Sort the Eigen values in decreasing order, the bigger the value the more important it represents
Evalsorted = np.sort(Eval)[::-1]

Index = np.argsort(Eval)[::-1]

# Sort the Eigen vectors depend on its values
Evecsorted = Eigenvec[:, Index]


Ppca = Evecsorted[:, :L] #Basis principal-component vectors

#Final data
Z = np.dot(X, Ppca) #Reducing the dimensionality

print('Original Data:')
print(XX)
print('Principal Component Basis Vectors:')
print(Ppca)
print('Transformed Data:')
print(Z)

# Specify the output CSV file name
output_file = 'outO.csv'

csv_out_path = os.path.join("csv/", "official/", output_file)

# Write the matrix to the CSV file (create the file if it doesn't exist)
with open(csv_out_path, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)

    # Write the header row if needed (uncomment this line if your data includes headers)
    # csv_writer.writerow(['Header1', 'Header2', 'Header3'])

    for row in Z:
        csv_writer.writerow(row)


# Extract columns (variables) from the data
variable1 = Z[:, 0]
variable2 = Z[:, 1]
variable3 = Z[:, 2]

# Create a plot using row numbers as time (x-axis)
x = np.arange(len(variable1))

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x, variable1, label='Variable 1')
plt.plot(x, variable2, label='Variable 2')
plt.plot(x, variable3, label='Variable 3')

# Customize the plot
plt.title('Variables Over Time')
plt.xlabel('Time Step (Row Number)')
plt.ylabel('Value')
plt.legend()

# Display the plot
plt.grid(True)
plt.show()