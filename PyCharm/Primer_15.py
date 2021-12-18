#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Эта программа показывает работу декоратора, который производит оптимизацию
# хвостового вызова. Он делает это, вызывая исключение, если оно является его
# прародителем, и перехватывает исключения, чтобы вызвать стек.

import sys
import timeit
from functools import lru_cache


@lru_cache
def factorail_nrec(n):
    factorial = 1
    while n > 1:
        factorial *= n
        n -= 1
    return n


@lru_cache
def factorail_rec(n, acc=1):
    if n == 0:
        return acc

    return factorail_rec(n - 1, n * acc)


@lru_cache
def fib_nrec(n):
    fib1 = 1
    fib2 = 1
    i = 0
    while i < n - 2:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        i = i + 1
    return fib2


@lru_cache
def fib_rec(i, current=0, next=1):
    if i == 0:
        return current
    else:
        return fib_rec(i - 1, next, current + next)


if __name__ == '__main__':
    numbers = 1000
    sys.setrecursionlimit(10000)
    start_time = timeit.default_timer()
    factorail_nrec(numbers)
    print("Время, затраченное на выполнение данного кода factoruil_nrec = ", timeit.default_timer() - start_time)
    start_time = timeit.default_timer()
    factorail_rec(numbers)
    print("Время, затраченное на выполнение данного кода factoruil_rec = ", timeit.default_timer() - start_time)
    start_time = timeit.default_timer()
    fib_nrec(numbers)
    print("Время, затраченное на выполнение данного кода fib_nrec = ", timeit.default_timer() - start_time)
    start_time = timeit.default_timer()
    fib_rec(numbers)
    print("Время, затраченное на выполнение данного кода fib_rec = ", timeit.default_timer() - start_time)

