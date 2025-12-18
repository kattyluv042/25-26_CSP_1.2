# Make 3 methods following these details:
# Method 1: name it "tic" and it takes 2 parameter- "num1" "num2"
# Returns the value of the 2 parameters when subtracted (ie; Num1 - Num2)
def tic(num1, num2):
    difference = num1 - num2
    return difference
print(tic(3, 9))
# Alternate answer: return num1  - num2

# Method 2: name it "tac" it takes 1 parameter- "exp"
# Use a loop to multiply the number 5 by itself "exp" times
# Return that value
def tac(exp):
    for product in range(exp):
        product =  5
    return product


# Method 3: name it "toe" that takes no parameters. This method should print
# The results of a method call to "tic(3, 5)" and "tac(4)" to the console
def toe():
    print(tic(3, 5))
    print(tac(4))
print(toe())