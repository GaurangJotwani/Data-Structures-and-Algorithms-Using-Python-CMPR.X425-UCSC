############################################################
# L0322Test.py
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2020
###########################################################

############################################################
#              NOTHING CAN BE CHANGED IN THIS FILE
###########################################################

############################################################
# All imports
###########################################################
from L0322 import *
from typing import List
from time import process_time


class L0322Test:
    def __init__(self):
        self._show = True
        self._num = 0
        self._test()

    def _test1(self, coins: 'List[int]', amount: int, eans: 'int'):
        self._num = self._num + 1
        print("______________________Problem", self._num,
              "---------------------------------")
        work = [0]
        changes = []
        p = L0322(coins, amount, changes, work, self._show)
        num_change = len(changes)
        if (num_change == 1):
            if (changes[0] == -1):
                num_change = -1
        if (self._show == False):
            print("Expected minimal change is", eans,
                  ". your answer is", num_change)
        if (num_change != eans):
            print("Expected minimal change is", eans,
                  ". But your answer is", num_change)
            assert(False)
        if (num_change != -1):
            s = 0
            for e in changes:
                s = s + e
            if (s != amount):
                print("You are giving me", amount,
                      ".But you should give me", s, "> I will call cops")
                assert(False)
        if (amount):
            if (work[0] == 0):
                print("How did you solve the problem witj no work?")
                assert(False)
            else:
                print("WORK = ", work[0])

    def _test(self):
        self._show = True
        w = [1, 3, 4]
        c = 6
        e = 2
        self._test1(w, c, e)

        w = [1, 2, 6, 10, 24, 30, 90]
        c = 100
        e = 2
        self._test1(w, c, e)

        w = [1, 2, 6, 10, 24, 30, 90]
        c = 34
        e = 2
        self._test1(w, c, e)

        w = [1, 5, 10, 25]
        c = 25
        e = 1
        self._test1(w, c, e)

        w = [1, 5, 10, 25]
        c = 16
        e = 3
        self._test1(w, c, e)

        w = [1]
        c = 0
        e = 0
        self._test1(w, c, e)

        w = [1]
        c = 1
        e = 1
        self._test1(w, c, e)

        w = [1]
        c = 2
        e = 2
        self._test1(w, c, e)

        w = [2]
        c = 3
        e = -1
        self._test1(w, c, e)

        self._show = False
        w = [186, 419, 83, 408]
        c = 6249
        e = 20
        self._test1(w, c, e)

        self._show = False
        w = [474, 83, 404, 3]
        c = 264
        e = 8
        self._test1(w, c, e)

############################################################
# main
# YOU CANNOT CHANGE ANYTHING BELOW
###########################################################


def main():
    print("Testing L0322Test Starts")
    s = L0322Test()
    print("Testing L0322Test ENDS")


############################################################
#
###########################################################
if (__name__ == '__main__'):
    main()
