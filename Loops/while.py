# print hello 10 times
# i = 1
# while i <= 10:
#     print("hello")
#     i+=1

# print backward counting from 5 to 1
# i = 5
# while i >= 1:
#     print(i)
#     i-=1
# print("Loop Ended")

# print forward counting from 1 to 5
# i = 1
# while i <= 5:
#     print(i)
#     i+=1
# print("Loop Ended")

# print forward counting from 1 to 100
# i = 1
# while i <= 100:
#     print(i)
#     i+=1
# print("Loop Ended")

# print numbers from 100 to 1
# i = 100
# while i >= 1:
#     print(i)
#     i-=1
# print("Loop Ended")

# print the multiplication table of a number n
# i = 1
# while i <= 10:
#     # print(8 * i)
#     print("8 x", i , "=", 8 * i)
#     i+=1
# print("Loop Ended")

# # print squares of a nums
# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# idx = 0
# while idx < len(nums):
#     print(nums[idx])
#     idx+=1

# heroes = ["ironman", "thor", "batman", "superman"]
# idx = 0
# while idx < len(heroes):
#     print(heroes[idx])
#     idx+=1

# nums = [1,4,9,16,25,36,49,64,81,100]
# x = 50

# i = 0
# while i < len(nums):
#     if(nums[i] == x):
#         print("Found at index", i)
#         break
#     i +=1
# else:
#      print("Sorry this square is not defined")

# letters = ['a' ,'f', 'i', 'p', 'o', 'u', 't', 'e']

# for ch in letters:
#     if ch in ['a','e','i','o','u']:
#         print(ch , "is a vowel")
#     else:
#         print(ch, "is a consonant")

names = ["atya", "anasa", "anamta", "asha"]
for ch in names:
    if len(ch) == 4:
        print(ch, " is accurate name")
    else:
        print(ch, " is inaccurate name")

for i in range(1,12):
    if i % 2 == 0:
        print(i, "is even")
    else:
        print(i, "is odd")