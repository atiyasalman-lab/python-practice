# area of triangle = 1/2 * base * height
triangle = {
    "base" : int(input("Enter the base : ")),
    "height" : int(input("Enter the height : "))
}
result = (
    ((1/2 * triangle["base"] * triangle["height"]))
)
print("Result:" , result)