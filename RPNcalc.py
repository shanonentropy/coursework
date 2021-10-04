#!/usr/bin/env python
#
import re
import math

def RPNcalc(s):
    # print (s)
    stack = []
    FloatType = type(1.23)
    IntType = type(3)
    for i in range(len(s)):
        x = s[i]
        # Push numbers onto stack
        if (type(s[i]) is FloatType) or (type(s[i]) is IntType):
            stack.append(s[i])

        elif s[i] == '+':
            x = stack.pop()
            y = stack.pop()
            stack.append(x+y)

        elif s[i] == '*':
            x = stack.pop()
            y = stack.pop()
            stack.append(x*y)

        elif s[i] == 'sin':
            x = stack.pop()
            stack.append(math.sin(x))

        # enter: copy last element on stack
        elif (s[i] == 'e') or (s[i] == 'E'):
            x = stack.pop()
            stack.append(x)
            stack.append(x)

        # Unrecognized commands
        else:
            break

    return stack.pop()

