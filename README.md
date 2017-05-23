# libpython
libpython is a library of Python code snippets for learning problem solving & developing efficient code

## What is libpython?

libpython was created to help out the people who are writing code as well as those who want to write better code. Beginners as well as experienced users can submit their code here, other users try to improve that code, make it faster, better and more readable. With this, people looking for a solution for their problem can find how they can solve their problem in the best possible manner by looking at the code which was developed and reviewed by many people.

## How to submit your code?
The code should be well commented because this is more like an __educational__ initiative, so beginners can learn how to write code practically and learn how experienced programmers solve the problems.

### What to consider before submitting your code
- Code should contain a comment about what it does at the beginning.
- Code should be modular, it should be easy to understand and edit for others.
- Code should be well commented so that the people who read it can understand the working easily.
- Credits\
In case the code you're submitting code that is not written by you then mention the person who has written it
If you've found that code on Stack Overflow then give the link. Give them credits which they deserve :smile:

### Code Sample
The code should be written in the following manner to maintain consistency and uniformity. 
```python 
# Description: This function takes n number of arguments as an list and then cubes them 
def cubelife(*args):
    cubed = []  # To store cubes of nubmer 
    for number in args:
        # Appending cubes of each number to cubed list
        cubed.append(number * number * number) 
    return cubed
# Code written by: John Doe 
# https://stackoverflow.com/questions/2252017/how-to-submit-code-for-libpython
```

## Story
One day I was writing a scipt which included writing a function to divide a list of numbers into n number of groups I was unable to find any python function that could do the job for me. I ended up making an inefficent function which was very complicated for doing such an easy task. I thought how awesome it'd be if few people could come together and develop snippets of Python code, in that way we will endup with most efficient code for doing the job. 

And the idea of making a Github repository for this task came in my mind. I thought about it for a while, such a repository will also help beginners to learn problem solving in an effective way. The repository would also help out people who want code to do a specific task but are not skilled enough to write an effective and efficient solution for their problem.

So here it is "libpython", where people contribute and work on each others' code to learn different approach towards solving a specific problem.

## Do us a favour 
Share this repository with your friends and other Python users so they can contribute to this repository and learn how to write code more effectively and efficiently. This will benefit the whole community as the experienced developers' knowledge will pass to begineers.
