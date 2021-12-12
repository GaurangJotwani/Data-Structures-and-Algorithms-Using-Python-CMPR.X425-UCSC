############################################################
# Selectionday.py
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2021
###########################################################

############################################################
#        NOTHING CAN BE CHANGED IN THIS FILE
###########################################################

############################################################
# All imports
###########################################################
from Solution import *
from Util import *
import math
import random


class Selectionday():
    def __init__(self):
        self._show = False
        self._u = Util()
        self._testBench()

    # Private function
    def _expectedAnswer(self, a: 'list'):
        ans = [0, 0, 0]
        for i in range(25):
            if (a[i] == 0):
                ans[0] = i
            elif (a[i] == 1):
                ans[1] = i
            elif (a[i] == 2):
                ans[2] = i
        return ans

      # Private function
    def _assertAnswer(self, r, e):
        for i in range(3):
            if (r[i] != e[i]):
                return False
        return True

    def _testBench(self):
        self._tests()
        self._testn()
        print("ALL TESTS PASSED")

    # Private function
    def _test1(self, a: 'List'):
        ranks = [0, 0, 0]  # populate the student ranks
        num_races = [0]  # MUST fill number of races conducted
        s = Solution(a, num_races, ranks, self._show)
        ans = self._expectedAnswer(a)
        if (self._show):
            self._u.print_index(25)
            self._u.print_list(a)
            print("expected ans:", ans)
            print("You took", num_races[0], "races")
        if (self._assertAnswer(ranks, ans) == False):
            print("Your answer is WRONG")
            assert(False)
        if (num_races[0] < 7):
            print("It is impossible to solve this problem in",
                  num_races[0], "races")
            assert(False)

    # Simple tests
    def _tests(self):
        self._show = True
        a = [17, 6, 18, 19, 11, 14, 1, 3, 16, 0, 9, 24,
             22, 4, 5, 15, 2, 8, 13, 12, 23, 21, 7, 20, 10]
        self._test1(a)

        a = [5, 11, 4, 15, 23, 0, 10, 19, 17, 1, 24, 6,
             12, 20, 7, 8, 22, 3, 21, 14, 18, 16, 9, 13, 2]
        self._test1(a)

        a = [0, 20, 12, 11, 23, 15, 3, 14, 24, 22, 18, 7,
             17, 6, 13, 21, 16, 19, 8, 5, 10, 1, 2, 4, 9]
        self._test1(a)

    # Random tests
    def _testn(self):
        self._show = False
        N = 1000
        print("Running", N, "races")
        for i in range(N):
            a = self._u.generate_suffled_number_between_1_to_n(25)
            self._test1(a)
        print("ALL ", N, " Races Passed")


############################################################
# main
# YOU CANNOT CHANGE ANYTHING BELOW
###########################################################
def main():
    print("Testing SelectiondayBase.py Starts")
    s = Selectionday()
    print("Testing SelectiondayBase.py ENDS")


############################################################
# Real main
###########################################################
if (__name__ == '__main__'):
    main()
