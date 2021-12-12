import math
import random

############################################################
# Solution.py
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2021
###########################################################

############################################################
# All imports
###########################################################


class Solution:
    def __init__(self, a: 'list of runtime', num_races: 'list of size 1', r: 'list of 3 best students', show: 'bool'):
        self.N = 25  # Number of students
        self.S = 3  # First 3 winners
        self.T = 5  # Number of tracks

        self._a = a  # List of run time (Given)
        self._num_races = num_races  # MUST fill number of races conducted
        self._r = r  # Find first 3 students (Must fill)

        self._show = show  # Must print how you conducted races is _show is True
        self._heap = self.Min_Heap()
        self._alg(self._r)

        # YOU CAN HAVE ANY NUMBER OF DATA STRUCTURES HERE

    class Min_Heap:
        def __init__(self):
            self._heap = [1000000000000]
            self._pos = 0

        def __str__(self):
            l = '[ '
            for i in range(self._pos):
                l = l + f"{self._heap[i+1]} "
            l = l + ']'
            return l

        def build_from_list(self, l):
            for item in l:
                self.insert(item)

        def size(self):
            return self._pos

        def isEmpty(self):
            return self._pos == 0

        def left(self, x):
            n = x*2
            if n <= self._pos:
                return self._heap[n]
            return None

        def right(self, x):
            n = x*2 + 1
            if n <= self._pos:
                return self._heap[n]
            return None

        def father(self, x):
            n = x // 2
            if n >= 1:
                return self._heap[n]
            return None

        def getTop(self):
            if self.isEmpty() == False:
                return self._heap[1]
            return None

        def insert(self, item):
            self._pos += 1
            self._heap.append(item)
            n = self._pos
            while n > 1:
                if self._heap[n][1] < self.father(n)[1]:
                    self._swap_values(n, n//2)
                    n = n//2
                    continue
                break

        def delete(self):
            if self.isEmpty():
                return None
            x = self._heap.pop()
            if self._pos == 1:
                self._heap = [1000000000000]
                self._pos = 0
                return x
            y = self.getTop()
            self._heap[1] = x
            self._pos -= 1
            n = 1
            while 2*n <= self._pos:
                if 2*n <= self._pos and 2*n+1 <= self._pos:  # if left and right child exists
                    if self.left(n)[1] <= self.right(n)[1] and self.left(n)[1] < x[1]:
                        self._swap_values(n, 2*n)
                        n = 2 * n
                        continue
                    elif self.right(n)[1] < self.left(n)[1] and self.right(n)[1] < x[1]:
                        self._swap_values(n, 2*n+1)
                        n = 2 * n + 1
                        continue
                    break
                if 2*n <= self._pos and 2*n+1 > self._pos:  # only left child exists
                    if self.left(n)[1] < x[1]:
                        self._swap_values(n, 2*n)
                        n = 2 * n
                        continue
                    break
            return y

        def _swap_values(self, index1, index2):
            x = self._heap[index1]
            self._heap[index1] = self._heap[index2]
            self._heap[index2] = x

   ############################################################
   # WRITE YOUR CODE BELOW
   # YOU CAN HAVE ANY NUMBER OF CLASSES AND PRIVATE FUNCTION
   # if self._show = True MUST SHOW ALL RACES
   # Must return NUMBER OF RACES
   ###########################################################

    def _alg(self, r):
        self._num_races[0] = 0  # FILL THIS
        self._r = [0, 0, 0]  # FILL THIS
        # First run all 25 horses. Total of 5 races
        results = []
        l = []
        for n in range(len(self._a)):
            if n % 5 == 0 and n != 0:
                results.append(self._race_five_horses(l))
                l = []
                l.append([n, self._a[n]])
            elif n == len(self._a)-1:
                l.append([n, self._a[n]])
                results.append(self._race_five_horses(l))
                l = []
            else:
                l.append([n, self._a[n]])
        # Race the fastest horse in each group. Sixth race
        for a in results:
            l.append(a[0])
        r[0] = self._race_five_horses(l)[0][0]
        arranged = [0, 0, 0, 0, 0]
        # arrange groups by fastest runners
        for i in range(len(l)):
            arranged[i] = results[l[i][0] // 5]
        # Now race the horses closes to the fastest runner. This will be 7th race
        final_race_contestants = []
        for i in range(3):
            if i == 0:
                final_race_contestants.append(arranged[0][1])
                final_race_contestants.append(arranged[0][2])
            if i == 1:
                final_race_contestants.append(arranged[1][0])
                final_race_contestants.append(arranged[1][1])
            if i == 2:
                final_race_contestants.append(arranged[2][0])
        final_race_contestants = self._race_five_horses(final_race_contestants)
        r[1] = final_race_contestants[0][0]
        r[2] = final_race_contestants[1][0]

    def _race_five_horses(self, l: 'list of T elements'):
        '''
        this function takes in a list of self.T elements
        returns a sorted list from fastest to slowest
        increases num of races by 1
        '''
        self._num_races[0] += 1

        self._heap.build_from_list(l)
        for i in range(self.T):
            l[i] = self._heap.delete()
        return l
