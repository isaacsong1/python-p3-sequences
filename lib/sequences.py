#!/usr/bin/env python3

def print_fibonacci(length):
    # if length == 0:
    #     print([])
    # elif length == 1:
    #     print([0])
    # else:
    #     fibonacci_array = [0, 1]
    #     if length > 2:
    #         for i in range(length - 2):
    #             fibonacci_array.append(fibonacci_array[i + 1] + fibonacci_array[i])
    #     print(fibonacci_array)

    # Solutions (I think the solution is clearer)
    fibonacci_array = []
    if length > 0:
        fibonacci_array.append(0)
    if length >= 2:
        fibonacci_array.append(1)
        for i in range(2, length):
            fibonacci_array.append(fibonacci_array[-1] + fibonacci_array[-2])
    print(fibonacci_array)