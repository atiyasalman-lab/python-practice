# def sum(a,b):
#     s = a + b
#     return s

# print(sum(2,3)) 

# def difference(b,a):
#     d = b - a
#     return d
# print(difference(6,4))

def count_elements(data):
    count = 0
    for i in data:
        count+=1
    return count


print(count_elements([1,2,3,4,5,"abc",8,"mnb",10]))

