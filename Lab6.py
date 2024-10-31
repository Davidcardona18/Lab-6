# David Cardona
# Assignment 6
# October 31, 2024

import random
import math

def problem_1():
    # Use a for statement and random.randrange to return 10 random integers between 25 and 35
    a = 25
    b = 35
    for _ in range(10):
        print(random.randrange(a, b + 1))

def problem_2():
    # Use random.randrange to return an odd integer between 0 and 100
    a = 0
    b = 100
    odd_number = random.randrange(a + 1, b, 2)
    print(odd_number)

def problem_3():
    # Use random.choice to select a day of the week from a list and return that day
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    day = random.choice(days)
    print(day)

def pi_approximation():
    # Calculate an approximation for pi using the Leibniz series and print the value along with math.pi
    pi_approx = 4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + 1/13)
    print(f"Approximation of pi: {pi_approx}")
    print(f"Value of math.pi: {math.pi}")

def conversion(rad):
    # Convert radians to degrees and print the value along with the value using math.degrees
    degrees = rad * (180 / math.pi)
    print(f"Calculated degrees: {degrees}")
    print(f"Using math.degrees: {math.degrees(rad)}")

def factorial_iterative(n):
    # Use a for statement to calculate the factorial of n
    result = 1
    for i in range(2, n + 1):
        result *= i
    print(f"Factorial of {n} (iterative): {result}")

def factorial_recursive(n):
    # Calculate the factorial of n using recursion (extra credit)
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

def main():
    # call your functions here
    print("Problem 1:")
    problem_1()
    print("\nProblem 2:")
    problem_2()
    print("\nProblem 3:")
    problem_3()
    print("\nPi Approximation:")
    pi_approximation()
    print("\nRadians to Degrees Conversion:")
    conversion(1)  # example value in radians
    print("\nFactorial (Iterative):")
    factorial_iterative(5)  # example value
    print("\nFactorial (Recursive):")
    print(f"Factorial of 5 (recursive): {factorial_recursive(5)}")  # example value

if __name__ == "__main__":
    main()
