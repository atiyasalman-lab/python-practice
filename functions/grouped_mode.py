classes = [(0,10),(10,20),(20,30),(30,40),(40,50)]
f = [5,8,12,7,3]
# modal _idx =  The most common value in a numerical array-  (i)
i = f.index(max(f))
L= classes[i][0]
start, end = classes[0]
h = end - start


mode = L +((f[i] - f[i - 1])/ (2*f[i]- f[i- 1] - f[i + 1])) * h
print("Mode is", mode)


# def mode(f):
#     i = f.index(max(f))
#     L= classes[i][0]
#     start, end = classes[0]
#     h = end - start
#     mode = L +((f[i] - f[i - 1])/ (2*f[i]- f[i- 1] - f[i + 1])) * h
#     return mode 
# classes = [(0,10),(10,20),(20,30),(30,40),(40,50)]
# f = [5,8,12,7,3]
# print("Mode is", mode)

