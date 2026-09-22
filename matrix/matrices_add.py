# def add(matrix_a, matrix_b):
#     result = []
#     for i in range(len(matrix_a)): #2
#         row = []
#         for j in range(len(matrix_a[0])): #2
#             row.append(matrix_a[i][j] + matrix_b[i][j])
#         result.append(row)
#     return result


# # matrix_a = [[1,2],
# #             [3,4]]

# # matrix_b = [[5,6],
# #             [7,8]]

# matrix_a = [[1,2,3],
#             [4,5,6],
#             [7,8,9]
#             ]

# matrix_b = [[9,8,7],
#             [6,5,4],
#             [3,2,1]
#             ]


# print("Add", add(matrix_a, matrix_b))


import numpy as np

# Create two matrices (NumPy arrays)
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

# Add the matrices using numpy.add()
matrix_sum = np.add(matrix_a, matrix_b)

# Print the result
print("Sum (using numpy.add()):")
print(matrix_sum)
