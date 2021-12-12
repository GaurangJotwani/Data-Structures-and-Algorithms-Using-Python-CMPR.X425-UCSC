############################################################
# Hash.py
# Hash oblect
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2021
###########################################################

############################################################
#  All imports here
###########################################################
from Slist import *


############################################################
#  class  Hash
###########################################################

class Hash():
    def __init__(self, size: 'int'):
        # WRITE YOUR DATA STRUCTURE HERE
        self._table_size = size
        self._bucket = []
        self._create_buckets(self._bucket)

    #############################
    # WRITE All public functions BELOW
    # YOU CAN HAVE ANY NUMBER OF PRIVATE FUNCTIONS YOU WANT
    #############################
    def insert(self, value):
        i = self._hash_func1(value)
        t = self._bucket[i]
        if t == 0:
            s = Slist()
            s.append(value)
            self._bucket[i] = s
        else:
            t.append(value)

    def __len__(self):
        i = 0
        for n in self._bucket:
            if n != 0:
                i += len(n)
        return i

    def statistics(self):
        if len(self) == 0:
            return (0, 0)
        maximum, minimum = 0, 0
        for n in self._bucket:
            if n != 0:
                n = len(n)
                if maximum == 0 or minimum == 0:
                    maximum, minimum = n, n
                else:
                    if n > maximum:
                        maximum = n
                    if n < minimum:
                        minimum = n
        return (minimum, maximum)

    def find(self, value):
        i = self._hash_func1(value)
        t = self._bucket[i]
        if t == 0:
            return False
        else:
            return t.find(value)

    def delete(self, value):
        i = self._hash_func1(value)
        t = self._bucket[i]
        if t == 0:
            pass
        else:
            t.delete(value)

        #############################
        # WRITE All private functtions BELOW
        # YOU CAN HAVE ANY NUMBER OF PRIVATE FUNCTIONS YOU WANT
        #############################

    def _create_buckets(self, l):
        for _ in range(self._table_size):
            l.append(0)

        #############################
        # Time:   THETA(1)
        # Space:  THETA(1)
        # NOTHING CAN BE CHANGED BELOW
        #############################
    def _hash_func1(self, key: 'int'):
        key = ~key + (key << 15)
        key = key ^ (key >> 12)
        key = key + (key << 2)
        key = key ^ (key >> 4)
        key = key * 2057
        key = key ^ (key >> 16)
        return key % (self._table_size)

    #############################
    # Time:   THETA(1)
    # Space:  THETA(1)
    # NOTHING CAN BE CHANGED BELOW
    #############################
    def _hash_func(self, key: 'int'):
        return key % (self._table_size)


h = Hash(100)
# print(h._buckets)
