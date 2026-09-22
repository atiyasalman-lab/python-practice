# mean = sum of all observation / total no. of observation
def mean(numbers):
    # numbers - [2, 3]
    result = sum(numbers) / len(numbers)
    return result


# formula for median odd = (n+1/2)
# formula for median even = (n/2 + n/2 + 1)/2

def median(numbers):
    numbers.sort()
    n = len(numbers)
    print("Sorted List:", numbers)
    if n % 2 != 0:
        median = numbers[int((n+1)/2) - 1]
        return median
    else:
        sec_num_idx = int(n/2) # 6/2 = 3
        first_num_idx = sec_num_idx - 1 # 3 - 1 = 2
        median = mean([numbers[first_num_idx], numbers[sec_num_idx]])
        return median
        


data = [1,2,3,1,8,7]
print("Median", median(data))


# numbers[3.0]


