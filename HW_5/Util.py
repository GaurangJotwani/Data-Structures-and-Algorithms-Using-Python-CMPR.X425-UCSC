import sys  # For getting Python Version
import random
import math


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Util():
    pass

    ############################################
    # generate_random_number start to end INCLUDED
    # start to end INCLUDED
    #########################################
    def generate_a_random_number(self, start: int, end: int) -> 'int':
        v = random.randrange(start, end+1)
        return v

    ############################################
    # generate_random_number GENERATES  N random numbers betweem
    # start to end INCLUDED
    # if onlypositive is False, generates both pos and negative number
    #  randrange(beg, end, step) :-
    #  beginning number (included in generation),
    #  last number (excluded in generation) a
    #  nd step ( to skip numbers in range while selecting).
    #########################################
    def generate_random_number(self, N: int, onlypositive: bool, start: int, end: int) -> 'List of integer':
        a = []
        for i in range(N):
            v = self.generate_a_random_number(start, end)
            if (onlypositive == False):
                if ((i % 2) == 0):  # //Even. Half are positive, Half are negative
                    v = -v
            a.append(v)
        return a

    ############################################
    # swap
    #########################################
    def swap(self, a: 'List of integer', i: 'int', j: 'int'):
        t = a[i]
        a[i] = a[j]
        a[j] = t

    ############################################
    # generate shuffled number between 0 to n
    # n-1 not encluded
    #########################################
    def generate_suffled_number_between_1_to_n(self, n: int) -> 'List of integer':
        a = []
        for i in range(n):
            a.append(i)

        for i in range(n):
            j = self.generate_a_random_number(0, n-1)
            k = self.generate_a_random_number(0, n-1)
            self.swap(a, j, k)
        return a

    ############################################
    # generate n numbers in ascending order from 0 to n-1
    #########################################
    def generate_n_numbers_in_ascending_order(self, n: int) -> 'List of integer':
        a = []
        for i in range(n):
            a.append(i)
        return a

    ############################################
    # generate n numbers in descending order from n-1 to 0
    #########################################
    def generate_n_numbers_in_desscending_order(self, n: int) -> 'List of integer':
        a = []
        for i in range(n-1, -1, -1):
            a.append(i)
        return a

    ############################################
    # generate n same k number
    #########################################
    def generate_n_same_k_number(self, n: int, k: 'int') -> 'List of integer':
        a = []
        for i in range(n):
            a.append(k)
        return a

    ############################################
    # print_index(10)
    #    0   1   2   3   4   5   6   7   8   9
    #########################################
    def print_index(self, n: int):
        for i in range(n):
            print("{:4d}".format(i), end="")
        print()

    ############################################
    # a = [7,8,9, 23, 100]
    # print_list(a)
    # 7   8   9  23 100
    #########################################
    def print_list(self, a: 'list'):
        for i in range(len(a)):
            print("{:4d}".format(a[i]), end="")
        print()

    ############################################
    # a = [7,8,9, 1, 100]
    # crash
    #########################################
    def assert_ascending_range(self, a: 'list', start: int, includingend: int):
        t = a[start]
        for i in range(start+1, includingend):
            if (a[i] < t):
                assert(False)
            t = a[i]

    ############################################
    # a = [7,8,9, 1, 100]
    # crash
    #########################################
    def assert_ascending(self, a: 'list'):
        if (len(a)):
            self.assert_ascending_range(a, 0, len(a))

    ############################################
    # log to the next possible integer
    #########################################
    def log_upper_bound(self, n: 'int', b: 'int') -> 'int':
        f = math.log(n, b)
        c = math.ceil(f)
        return c

    ############################################
    # log to the smallest possible integer
    #########################################
    def log_lower_bound(self, n: 'int', b: 'int') -> 'int':
        f = math.log(n, b)
        c = math.floor(f)
        return c

    ############################################
    # sqrt to the next possible integer
    #########################################
    def sqrt_upper_bound(self, n: 'int') -> 'int':
        f = math.sqrt(n)
        c = math.ceil(f)
        return c
