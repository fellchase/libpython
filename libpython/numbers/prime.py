# Description: Function for checking if given argument is a prime number or not.
#
# Natural numbers only divisible by 1 and themselves are known as prime numbers. 
# 
# Prime numbers have always fascinated programmers and computer scientists with its random
# pattern of occurrence. Mathematicians are still finding ways to next prime number without
# exhaustive computations. Gap between two consecutive prime numbers is called prime gap. If
# we are able to find prime gap, we can easily find the next prime number by simply adding
# the prime gap and known prime number. Finding prime gap is still unsolved problem and if
# you think it shouldn't be so hard, read this: http://mathworld.wolfram.com/PrimeGaps.html
# 
# This function does exhaustive linear search by matching each number with remainder of all
# possible natural numbers. Function provides a little efficiency using the fact that 2 is
# the only even prime number and the other prime numbers are odd. So all the even numbers are
# excluded except 2 to gain some efficiency. Another point to gain efficiency is that multiples
# of any natural numbers will always be lower than the one third of the given number.
# Author: Vikrant Singh Chauhan | Contact: vi@divwebs.com


def prime(num):
    # num is actually a string because input() returns strings. We'll convert it to int
    num = int(num)

    if num in [1, 2, 3]:
        # if given argument is 1 2 or 3, it is prime. We used list without defining a variable which is perfectly valid
        return True
    if num % 2 == 0:  # excluding all even numbers except two.
        return False
    else:
        # Here we are starting counter variable from 3 in range. Second argument excludes numbers above one third
        # of the given argument. Third argument in range sets steps to take to 2. This makes loop to iterate odds
        for x in range(3, int(num/3), 2):
            # Checking if argument is divisible by counter. % is modulus operator which returns remainder of division
            if num % x == 0:
                return False
    # It's okay to have more than one return statement when program hits return statement it exits the function.
    return True

# Example: Useful for finding prime numbers
# Below is a short-hand if statement It outputs "Prime!" if prime() returns True. "Not a prime." otherwise
# Input received from user is passed to prime function which then returns a boolean value.
print(("Prime!" if prime(input("Enter a number: ")) else "Not a prime."))
