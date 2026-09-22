# quadratic equation - ax^2 + bx + c

question = "What is the value of the quadratic equation?"
equation = {
        "value of a": int(input("Enter the value of a : ")),
        "value of b": int(input("Enter the value of b : ")),
        "value of c": int(input("Enter the value of c : ")),
        "value of x": int(input("Enter the value of x : "))
}


# equation = {
#     "a": 1,
#     "b": 3,
#     "c": 2,
#     "x": 2
# }

result = (
    (equation["value of a"] * 
     equation["value of x"]**2) +
    (equation["value of b"] * equation["value of x"]) +
    equation["value of c"]
)
print(question)
print("Result:", result)