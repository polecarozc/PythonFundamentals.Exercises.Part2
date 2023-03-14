def exponentiator(num1):
    return num1**2

def raise_to_forth_power(num):
    return num**4
def cubed(num):
    return num**3

square = lambda s: exponentiator(s)

cube = lambda j: cubed(j)

print(square(2))
print(cube(2))
print(raise_to_forth_power(2))