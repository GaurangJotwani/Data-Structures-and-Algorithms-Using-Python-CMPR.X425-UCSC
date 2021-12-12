import sys  # For getting Python Version


############################################################
# RecursionTest.py
# Test Bench for Recursion
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2021
###########################################################

############################################################
#  NOTHING CAN BE CHANGED IN THIS FILE
###########################################################

############################################################
#  All imports here
###########################################################
# import sys # For getting Python Version
from Recursion import *

############################################################
#  class  test factorial
###########################################################


class Test_fact():
    def __init__(self):
        self._test()

    def _test1(self, n: 'int') -> 'void':
        o = Recursion()
        ans1 = o.factI(n)
        ans2 = o.factR(n)
        print("Fact(", n, ") Iterative = ", ans1, sep="")
        print("Fact(", n, ") Recursive = ", ans2, sep="")
        assert(ans1 == ans2)

    def _test(self):
        a = [0, 1, 5, 10, 20]
        for e in a:
            self._test1(e)

############################################################
#  class  test print asis
###########################################################


class Test_print_asis_reverse():
    def __init__(self):
        self._test()

    def _test1(self, n: 'int', reverse: 'bool') -> 'void':
        o = Recursion()
        if (reverse):
            print(n, " in reverse order is as follows")
        else:
            print(n, " in asis order is as follows")
        print("Iterative")
        o.printI(n, reverse)
        print("Recursive")
        o.printR(n, reverse)

    def _test(self):
        a = [0, 1, 9, 10, 1986, 1000, 1111, 5267896714578]
        for e in a:
            self._test1(e, True)
        for e in a:
            self._test1(e, False)

############################################################
#  class  reverse int
###########################################################


class Test_reverse():
    def __init__(self):
        self._test()

    def _test1(self, n: 'int') -> 'void':
        o = Recursion()
        ans1 = o.reverseI(n)
        ans2 = o.reverseR(n)
        print("Reverse(", n, ") Iterative = ", ans1, sep="")
        print("Reverse(", n, ") Recursive = ", ans2, sep="")
        assert(ans1 == ans2)

    def _test(self):
        a = [0, 1, 9, 10, 1986, 1000, 1111, 5267896714578]
        for e in a:
            self._test1(e)

############################################################
#  class  test fib
###########################################################


class Test_fib():
    def __init__(self):
        self._test()

    def _test1(self, n: 'int') -> 'void':
        o = Recursion()
        ans1 = o.FibI(n)
        ans2 = o.FibR(n)
        print("Fib(", n, ") Iterative = ", ans1, sep="")
        print("Fib(", n, ") Recursive = ", ans2, sep="")
        assert(ans1 == ans2)

    def _test(self):
        a = [0, 1, 9, 10, 14, 20]
        for e in a:
            self._test1(e)

############################################################
#  class  Test permutation
###########################################################


class Test_permutation():
    def __init__(self):
        self._test()

    def _fact(self, n: 'int') -> 'int':
        s = 1
        for i in range(2, n+1):
            s = s * i
        return s

    def _test(self):
        N = 5
        for n in range(N):
            o = Recursion()
            print("Permutation of ", n, "are as follows")
            a = o.permR(n)
            print("Num permutation = ", a)
            #assert(a == self._fact(n))

  ############################################################
# MAIN
###########################################################


def main():
    print("Basic Recursion test starts")
    print(sys.version)
    print("----------------Testing factorial--------------------")
    t = Test_fact()
    print("----------------Testing print asis/reverse--------------------")
    t = Test_print_asis_reverse()
    print("----------------Testing reverse--------------------")
    t = Test_reverse()
    if (False):
        print("----------------Testing Fibonacci--------------------")
        t = Test_fib()
        print("----------------Testing permutation by recursion--------------------")
        t = Test_permutation()
    print("Basic Recursion test Passed. If you don't see this line means, you cannot write Recursion")


main()
