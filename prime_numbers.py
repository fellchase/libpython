#!/usr/bin/env python

# Author: Vikrant Singh Chauhan
# Email: "vi@divwebs.com"

""" Function for checking if given argument is a prime number or not.

This function is just a simple algorithm to check if given number is prime or not.
Natural numbers only divisible by 1 and themselves are known as prime numbers. 

Prime numbers have always fascinated programmers and computer scientists with its random
pattern of occurrence. Mathematicians are still finding ways to next prime number without
exhaustive computations. Gap between two consecutive prime numbers is called prime gap. If
we are able to find prime gap, we can easily find the next prime number by simply adding
the prime gap and known prime number. Finding prime gap is still unsolved problem and if
you think it shouldn't be so hard, read this: http://mathworld.wolfram.com/PrimeGaps.html

This function does exhaustive linear search by matching each number with remainder of all
possible natural numbers. Function provides a little efficiency using the fact that 2 is
the only even prime number and the other prime numbers are odd. So all the even numbers are
excluded except 2 to gain some efficiency. Another point to gain efficiency is that multiples
of any natural numbers will always be lower than the one third of the given number.
"""


def prime(argv):
  if (argv in [1,2,3]):        # if given argument is 1 2 or 3, it is prime. See how we used list without defining a variable.
    return True
  if(argv % 2 == 0):            # excluding all even numbers except two.
    return False
  else:
    for x in range(3, int(argv/3), 2):     # here we are starting counter variable from 3 in range. Second argument excludes numbers above one third
                                           # of the given argument. Third argument in range sets steps to take to 2. This makes loop to iterate odds
      if (argv % x == 0):                  # this line checks if argument is divisible by counter.
        return False
  return True

print(("Prime!" if prime(int(input("Enter a number: "))) else "Not a prime."))
