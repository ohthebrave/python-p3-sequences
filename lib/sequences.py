#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        return []
    elif length == 1:
        return [1]

    fibo = [0,1]
    for i in range(2, length):
        fibo.append(fibo[i-1] + fibo[i-2])
    return fibo


print(print_fibonacci(9))