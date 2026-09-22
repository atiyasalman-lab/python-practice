users = [
    { "name": "Atiya", "yob": 2001 },
    { "name": "Anam", "yob": 2025 },
    { "name": "Asha", "yob": 1930 },
    { "name": "Aliya", "yob": 2010 },
    { "name": "Asiya", "yob": 1940 },
]

current_year = 2026
for user in users:
    age = current_year - user["yob"]
    if age >= 18:
        print(user["name"], "is", age , "years old and eligible to vote")
    else:
        print(user["name"], "is", age , "years old and not eligible to vote")
