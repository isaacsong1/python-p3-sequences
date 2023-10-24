#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print([])
    elif length == 1:
        print([0])
    else:
        fibonacci_array = [0, 1]
        if length > 2:
            for i in range(length - 2):
                fibonacci_array.append(fibonacci_array[i + 1] + fibonacci_array[i])
        print(fibonacci_array)