"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:         #enter the denominator loop
        print("Can not divided by 0")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)


except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

#Answer 1
# When I enter a non-numeric charactor like A, B, C.

#Answer 2
# When I enter a 0 into denominator

#Answer 3
# I did not get the point, but I think you want me to make the function continue instead of finishing it.