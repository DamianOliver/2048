import math

# input = input("Enter Number of Children: ")

# input = int(input)

# def calculate(input):
#     two_power = 2

#     while (two_power <= input):
#         two_power *= 2

#     two_power /= 2

#     output = (input-two_power) * 2 + 1

#     return output

import math

def calculate(n):
    last_2 = 2**int(math.log2(n))
    output = (n-last_2) * 2
    print(n, output)

def recursive(n):
    if n == 1:
        return 0
    return (recursive(n-1) + 2) % n

for i in range(2, 50):
    print(recursive(i))
