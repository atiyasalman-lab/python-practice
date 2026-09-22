users = [
    { "name": "Atiya", "age": 19 },
    { "name": "anam", "age": 25 },
    { "name": "Asha", "age": 30 },
    { "name": "Aliya", "age": 10 },
    { "name": "Asiya", "age": 40 },
]
# if age > 18:
#     print("You are eligible to vote")
# else:
#     print("You are not eligible to vote")

# for age in users:
#     print(age)

# print(users[0], "Eligible to vote")

# if person in users age > 18:
#     print(users[0], "Eligible to vote")
#     print(users[1], "Eligible to vote")
#     print(users[2], "Eligible to vote")
#     print(users[3], "Eligible to vote")
#     print(users[4], "Eligible to vote")
# else:
#     print(users[0], "not Eligible to vote")
#     print(users[1], "not Eligible to vote")
#     print(users[2], "not Eligible to vote")
#     print(users[3], "not Eligible to vote")
#     print(users[4], "not Eligible to vote")

# for person in users:
#     if users[age] > 18:
#         print(person["name"], "is eligible to vote")
#     else:
#         print(person["name"], "is not eligible to vote")

for user in users:
    if user["age"] >= 18:
        print(user["name"], "is eligible to vote") 
    else:
        print(user["name"], "is not eligible to vote")
        