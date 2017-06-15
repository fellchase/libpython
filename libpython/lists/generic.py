"""
# Generic list code snippets
# Code that is very huge for this file or not 'generic' will be placed separately in lists directory 
# For example list sorting algorithms would be in /lists/sorting/bubble_sort.py
"""


# Description: Useful for dividing a list of stuff into groups of same size, function will try to
# ceiling if list can't be divided which can cause trouble sometimes, like if you try to divide list of 10 numbers
# into 5 or 6 groups will result in same answer
# Author: fellchase
def partition_list(raw_list, ngroups):
    """
    param raw_list
    takes a list
    param ngroups
    takes an int
    returns a list with lists inside it
    """
    # Maximum elements in a single group
    # -(-x // n) Denotes ceiling, using only // floors the float
    # Ceiling means round up to next biggest int
    # floor means to round down to last biggest int
    # We have to ceiling the number otherwise it doesn't divide list into specified ngroups
    max_elems_in_group = -(-len(numbers) // ngroups)

    grouped_list = []
    group = []

    # enumerate gives us an index of the list its passed
    # Basically (0, elem1), (1, elem2) and so on, on each iteration
    for index, num in enumerate(numbers):
        group.append(num)

        # If its has reached the limit we append it to
        # grouped_list and empty the group variable
        if len(group) == max_elems_in_group:
            grouped_list.append(group)
            group = []

        # Checks if its the last iteration
        # index starts from 0 thus we add 1
        elif index + 1 == len(numbers):
            grouped_list.append(group)

    return grouped_list

# Example: Useful in case you want to divide task among few threads evenly pass a list, get it divided
# assign one group to one thread



# Description: Function below takes list as input then recursively scans for list and appends all of found elements
# in one single list which is returned at the end 
# Author: fellchase 
def make_flat_list(input_list):
    flat_list = []  # Temporary variable to append elements

    # Appends list to flat_list
    for x in input_list:
        if type(x) is not list:
            flat_list.append(x)
        elif type(x) is list:
            # If it's a list then we put it again in the same function, then it'll be handled by if block above
            # Now we could have just passed x instead of make_flat_list(x) in the for loop below but then if lists 
            # has more lists inside it they won't be flattened
            for y in make_flat_list(x):
            # After the list is passed to make_flat_list() in line above it'll return an list whose elements will be
            # appended to the flat_list
                flat_list.append(y)

    return flat_list
# Example: When you've more than 1 list in an list you can this function to flatten them out
# print(make_flat_list([1, [2, [3, [4], [5, 6], [7, 8]]]]))
# Output ==> [1, 2, 3, 4, 5, 6, 7, 8]
