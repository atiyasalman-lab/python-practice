# import math
# print(math.pi)
# # area = 1/2(a+b)*h

# # area = ((base_a + base_b)/2) * height
# trapezoid = {
#     "base_a": 10,
#     "base_b": 20,
#     "height": 5
# }
# result = (
#     ((trapezoid["base_a"] + trapezoid["base_b"])/2) * trapezoid["height"]
# )
# print("Result:", (result))
trapezoid = {
    "base_a" : int(input("Enter the base_a : ")),
    "base_b" : int(input("Enter the base_b : ")),
    "height" : int(input("Enter the height : "))
}
result = (
    ((trapezoid["base_a"] + trapezoid["base_b"])/2) * trapezoid["height"]
)
print("Result:" , result)