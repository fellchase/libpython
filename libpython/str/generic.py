"""
# Generic str code snippets
# Code that is very huge for this file or not 'generic' will be placed separately in lists directory 
# For example  sorting algorithms would be in /lists/sorting/bubble_sort.py
"""

# Description: Used to print Unicode escape characters which look like this \u03003\u03030
# Author: Jelle Fresen | Contact: https://stackoverflow.com/users/212115/jelle-fresen
# https://stackoverflow.com/questions/14630288/unicodeencodeerror-charmap-codec-cant-encode-character-maps-to-undefined

# from sys import stdout # You'll need to import stdout
# '*' in *objects means that all argument you pass will be combined into a list and passed to function
# except if you specify argument name
def uprint(*objects, sep=' ', end='\n', file=stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        # If encoding is UTF-8 then we just print normally
        print(*objects, sep=sep, end=end, file=file)
    else:
        # If that's not the case then we've to backslash replace
        # lambda is like a function
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        # map takes a list 'objects' & applies function 'f' on the list then returns the new list which is unpacked
        print(*map(f, objects), sep=sep, end=end, file=file)
# Example: It can be used in Windows CMD to print a Japanese characters which can't be printed on CMD, and program
# will handle the Unicode characters just fine


# Description: Shrinks str_to_fit if it's too long and space isn't available on command line, returns str_to_fit after
# making modifications if necessary
# Author: fellchase
def fit_str(str_to_fit, rest_of_string, columns):
    len_of_str_available = columns - len(rest_of_string)  # Max space available for str_to_fit; -1 for safety

    if len(str_to_fit) > len_of_str_available:  # We shrink str_to_fit If length is more than len_of_str_available
        if len_of_str_available <= 5:
            raise Exception("Not enough space to fit string")

        beginning_half = str_to_fit[:(len_of_str_available // 2) - 2]  # Less 3 chars, we be add three periods later
        ending_half = str_to_fit[-((len_of_str_available // 2) - 1):]
        str_to_fit = beginning_half + '...' + ending_half

    return str_to_fit

# Example: Useful if you're making a down loader or something and want to put ... in the long file names which you've to
# display on terminal
# from os import get_terminal_size
# 
# try:
#     columns = get_terminal_size()[0]
# except Exception:  # In case you're using IDE columns will be set to 80
#     columns = 80
# 
# pline = "Downloading 10MB file "
# file_name = "some_example_file_with_long_name.mp4"
# 
# line = pline + fit_str(file_name, pline, columns)
# print(line)
