# Function to interchange first and last columns of a matrix
def interchange_columns(matrix):
    rows = len(matrix)
    
    # Loop through each row and swap the first and last column elements
    for i in range(rows):
        matrix[i][0], matrix[i][-1] = matrix[i][-1], matrix[i][0]
    
    return matrix

# Input matrix (3x3)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Interchanging the first and last columns
result = interchange_columns(matrix)

# Output the resulting matrix
print("Matrix after interchanging first and last columns:")
for row in result:
    print(row)
