import sys  # For getting Python Version

############################################################
# Recursion.py
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2021
###########################################################

############################################################
#  All imports here
###########################################################

############################################################
#  class  test factorial
###########################################################


class Recursion():
    def __init__(self):
        # Nothing can be added here
        pass

    ############################################################
    #          WRITE ALL YOUR PUBLIC FUNCTION BELOW
    ###########################################################

    def factI(self, n):
        ans = 1
        for i in range(n):
            ans = ans * (i+1)
        return ans

    def factR(self, n):
        if n <= 1:
            return 1
        else:
            return n*self.factR(n-1)

    def printI(self, n, reverse):
        if n <= 9:
            print(n)
            return None
        if reverse:
            while n:
                print(n % 10, end=' ')
                n = n // 10
            print()
        else:
            l = []
            while n:
                l.append(n % 10)
                n = n // 10
            for i in range(len(l)):
                print(l[len(l)-i-1], end=' ')
            print()

    def printR(self, n, reverse):
        if reverse:
            if n <= 9:
                print(n)
            else:
                print(n % 10, end=' ')
                self.printR(n // 10, True)
        else:
            l = []
            l = self._printR_helper(l, n)
            for i in range(len(l)):
                print(l[len(l)-i-1], end=' ')
            print()

    def reverseI(self, num):
        test_num = 0
        while(num > 0):
            remainder = num % 10
            test_num = (test_num * 10) + remainder
            num = num//10
        return test_num

    def reverseR(self, num):
        res = 0
        return self._reverseR_helper(res, num)

    ############################################################
    #          WRITE ALL YOUR PRIVATE FUNCTION BELOW
    ###########################################################

    def _printR_helper(self, l, n):
        if n <= 9:
            l.append(n)
            return l
        else:
            l.append(n % 10)
            return self._printR_helper(l, n // 10)

    def _reverseR_helper(self, res, num):
        if num > 0:
            remainder = num % 10
            res = res * 10 + remainder
            return self._reverseR_helper(res, num // 10)
        return res
