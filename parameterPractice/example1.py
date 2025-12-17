'''# Method to add numbers
def add_numbers(one, two):
     sum = one + two
     return sum
'''
# Write a method that takes in 3 numbers
# Add the first two, and multiply by the third
# Return the result of the operation
def addAndmultiply_numbers(one, two, three):   # Return method
    product = (one + two) * three
    return product

def addAndmultiply_voidnumbers(one, two, three):
    product = (one + two) * three
    print(product)


print(addAndmultiply_numbers(9, 4, 3))

answer = addAndmultiply_voidnumbers(3, 4, 5)
print(answer)