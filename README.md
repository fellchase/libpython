# libpython

                                                                                                       
      88        88                                              ,d                                     
      88        88                                       ,d     88                                     
      88   88   88                                       88     88                                     
      88        88                                       88     88                                     
      88   88   88,dPPYba,   8b,dPPYba,   8b       d8  MM88MMM  88,dPPYba,    ,adPPYba,   8b,dPPYba,   
      88   88   88P'    "8a  88P'    "8a  `8b     d8'    88     88P'    "8a  a8"     "8a  88P'   `"8a  
      88   88   88       d8  88       d8   `8b   d8'     88     88       88  8b       d8  88       88  
      88   88   88b,   ,a8"  88b,   ,a8"    `8b,d8'      88,    88       88  "8a,   ,a8"  88       88  
      88   88   8Y"Ybbd8"'   88`YbbdP"'       Y88'       "Y888  88       88   `"YbbdP"'   88       88  
                             88               d8'                                                      
                             88              d8'     A library of Python 3 code snippets for learning  
                             88             d8'           problem solving & developing efficient code  
                                                                                                       

## What is libpython?

libpython was created to help out the people who are writing code as well as those who want to write better code. Beginners as well as experienced users can submit their code here, other users try to improve that code, make it faster, better and more readable. With this, people looking for a solution for their problem can find how they can solve their problem in the best possible manner by looking at the code which was developed and reviewed by many people.

## How to submit your code?
The code should be well commented because this is more like an __educational__ initiative, so beginners can learn how to write code practically and learn how experienced programmers solve the problems.

### What to consider before submitting your code
- Code should be in Python 3.
- Code should be modular & well commented.
- Make sure that the code and comments don't exceed 120 lines, so to be easily readable.
- In case your code contains some difficult to understand lines of code or syntax which beginners might not know about then please comment it well.
- Try to follow Python conventions and PEP in general for things like variable names, comments, etc.
- Credits\
In case the code you're submitting code that is not written by you then mention the person who has written it
If you've found that code on Stack Overflow then give the link. Give them credits which they deserve :smile:
- Format code according to the code sample given below before contributing.

### Code Sample
The code should be written in the following manner to maintain consistency and uniformity. 
```python 
# Description: This function takes n number of arguments as an list and then cubes them
# Author: John Doe | Contact(Optional): john.doe@mail.com
# https://stackoverflow.com/questions/2252017/how-to-submit-code-for-libpython
def cubelife(*args):
    cubed = []  # To store cubes of number 
    for number in args:
        # Appending cubes of each number to cubed list
        cubed.append(number * number * number) 
    return cubed
# Example: It can be used to make cubes of a list of numbers in a calculator script
# print(cubelife(2, 3, 4, 5))
# Output ==> [8, 27, 64, 125]
```

## Story
One day I was writing a script which included writing a function to divide a list of numbers into n number of groups I was unable to find any python function that could do the job for me. I ended up making an inefficient function which was very complicated for doing such an easy task. I thought how awesome it'd be if few people could come together and develop snippets of Python code, in that way we will end up with most efficient code for doing the job. 

And the idea of making a Github repository for this task came in my mind. I thought about it for a while, such a repository will also help beginners to learn problem solving in an effective way. The repository would also help out people who want code to do a specific task but are not skilled enough to write an effective and efficient solution for their problem.

So here it is "libpython", where people contribute and work on each others' code to learn different approach towards solving a specific problem.

## Do us a favour 
Share this repository with your friends and other Python users so they can contribute to this repository and learn how to write code more effectively and efficiently. This will benefit the whole community as the experienced developers' knowledge will pass to beginners.
