############################################################
# HashTest.py
# Test Bench for Hash
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2021
###########################################################

############################################################
#  NOTHING CAN BE CHANGED IN THIS FILE
###########################################################

############################################################
#  All imports here
###########################################################
import sys  # For getting Python Version
from Util import *
from Hash import *

############################################################
#  class  Hash test
###########################################################


class HashTest():
    def __init__(self):
        self._u = Util()
        self._test_int_hash()

    def _test1(self, N, B, S, E):
        print("------------------  TESTING add to hash ")
        print("------------------  Adding", N, "Random numbers between",
              S, "To", E, " Bucket size", B, "---------")
        print("Perfect hash should have exactly",
              N//B, "elements in each bucket")
        d = {}
        h = Hash(B)
        for i in range(N):
            v = self._u.generate_a_random_number(S, E)
            # Note v can have duplicate
            # If hash has to be like dict, we need to modify slist node with {key,val,next}
            # Python dict. key is i(unique) and value is v
            d[i] = v  # insert in dict
            h.insert(v)  # insert in hash
        assert(len(h) == N)
        assert(len(h) == len(d))
        [min, max] = h.statistics()
        print("MIN= ", min)
        print("MAX= ", max)
        print("Perfect hash should have exactly", len(h)//B, "elements")

        print("------------------  Testing find --------------")
        for key, value in d.items():
            v = h.find(value)
            assert(v)
        print("------------------  Testing delete --------------")
        print(h.statistics())
        for key, value in d.items():
            v = h.delete(value)
        print(h.statistics())

    def _test_int_hash(self):
        N = 100000
        B = N // 10
        S = 111111111
        E = 999999999
        self._test1(N, B, S, E)

        N = 500000
        B = N // 100
        S = 111111111
        E = 999999999
        self._test1(N, B, S, E)

        N = 1000
        B = N // 10
        S = 0
        E = 1000
        self._test1(N, B, S, E)
