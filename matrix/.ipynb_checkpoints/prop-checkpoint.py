#commutative property
import numpy as np

A = np.array([1,2,3])
B = np.array([4,5,6])
C = np.array([7,8,9])
O = np.array([0,0,0])
# result_1 = a+b
# result_2 = b+a

# print(result_1)
# print(result_2)

# result_1 = a*b
# result_2 = b*a
# print(result_1)
# print(result_2)

#Associative property = (A+B)+C = A+(B+C)
# result_1 = (A+B)+C
# result_2 = A+(B+C)
# print(result_1)
# print(result_2)

#Additive identity = A+0 = A = 0+A
# result_1 = A+O
# result_2 = O+A
# print(result_1)
# print(result_2)

#Additive inverse #inverse of a variable
# D = np.array([[1,-2,3],
#              [-4,5,6]])

# additive_inverse = -D
# print(additive_inverse)

#Distributive: A(B+C)=AB + AC and (B+C)A = BA + CA
result_1 =  A*(B+C)=A*B + A*C
result_2 = (B+C)*A = B*A + C*A

print(result_1)
print(result_2)

