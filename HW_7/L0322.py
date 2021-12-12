############################################################
# L0322.py
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2020
###########################################################

############################################################
# All imports
###########################################################
from typing import List
from time import process_time


class Solution:
    # YOU CANNOT CHANGE THIS INTERFACE
    # LEETCODE INTERFACE
    def coinChange(self, coins: List[int], amount: int) -> int:
        # YOU CANNOT CHANGE ANYTHING IN THIS PROCEDURE
        work = [0]
        changes = []  # If change cannot be given, you must put -1 in changes[0]
        show = False
        p = L0322(coins, amount, changes, work, show)
        num_change = len(changes)
        if (num_change == 1):
            if (changes[0] == -1):
                num_change = -1
        return num_change


class L0322:
    def __init__(self, coins: List[int], amount: 'int', changes: 'list of int', work: 'List of size 1', show: 'boolean'):
        # NOTHING CAN BE CHANGED
        self._d = coins
        self._n = amount
        self._ans = changes
        self._work = work
        self._show = show
        # YOU MUST GENERATE V table and k table
        self._v = []
        self._k = []
        # You can have any number of data structures here
        # MUST WRITE TWO ROUTINES
        self._alg()
        self._get_solution()

    def _increment_work(self):
        self._work[0] = self._work[0] + 1

    ############################################################
    # WRITE CODE BELOW
    ###########################################################

    ############################################################
    # TIME (n * k ) = O(n)
    # SPACE O(n)
    ############################################################
    def _alg(self):
        self._k.append(0)
        self._v.append(0)
        for i in range(1, self._n+1):
            min_coin = [-1]
            c = -1
            for coin in self._d:
                self._increment_work()
                a = i - coin
                if a < 0:
                    continue
                else:
                    if self._v[a] == -1:
                        continue
                    if min_coin[0] != -1:
                        if min_coin[0] > 1 + self._v[a]:
                            min_coin[0] = 1 + self._v[a]
                            c = coin
                    else:
                        min_coin[0] = (1 + self._v[a])
                        c = coin
            self._v.append(min_coin[0])
            self._k.append(c)

        a = self._n
        if self._v[a] == -1:
            self._ans.append(-1)
        else:
            while a > 0:
                self._ans.append(self._k[a])
                a = a - self._k[a]

    ############################################################
    # NOTHING CAN BE CHANGED IN THIS ROUTINE BELOW
    ###########################################################

    def _get_solution(self):
        if (self._show):
            a = []
            for i in range(self._n + 1):
                a.append(i)
            print(a)
            print(self._v)
            print(self._k)
        for i in range(self._n + 1):
            if (self._show):
                print("minimum change for", i,
                      "cents can be achieved using", self._v[i], "coins.")
                self._get_solution1(i)

    ############################################################
    # TIME O(n)
    # SPACE THETA(1)
    # How will you give change for p cents
    # WRITE CODE BELOW
    ############################################################
    def _get_solution1(self, p: 'int'):
        a = p
        b = 0
        counter = 1
        if p > 0:
            while a > 0:
                if self._k[a] == -1:
                    print(f"Change cannot be given for {p} cents")
                    break
                b = b + self._k[a]
                print(
                    f"{counter} : Give coin {self._k[a]}. So far you have given= {b}. Remaining to give {a - self._k[a]}")
                a = a - self._k[a]
                counter += 1
