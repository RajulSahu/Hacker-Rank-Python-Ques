#!/bin/python3

import math
import os
import random
import re
import sys

def solve(s):
    final_str = ""
    for word in s.split(" "):
        if word.isalpha():
            final_str += word[0].upper() + word[1:]
        else:
            final_str += word
        final_str += " "
    
    
    return final_str
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
