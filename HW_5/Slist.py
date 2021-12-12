############################################################
# Slist.py
# SList oblect
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2021
###########################################################

############################################################
#  All imports here
###########################################################
from ListNode import ListNode

############################################################
#  class  Slist
###########################################################

import sys  # For getting Python Version
import random
import math


class Slist():
    def __init__(self):
        # NOTHING CAN BE CHANGED HERE
        self._first = None
        self._last = None

    def __str__(self):
        string = ''
        current = self._first
        while current:
            string = string + f'{current.val}->'
            current = current.next
        return string + 'NULL'

    def __len__(self):
        n = 0
        current = self._first
        while current:
            n += 1
            current = current.next
        return n

    def prepend(self, value):
        s = ListNode(value)
        if self._first:
            s.next = self._first
            self._first = s
        else:
            self._first = s
            self._last = s

    def append(self, value):
        s = ListNode(value)
        if self._last:
            self._last.next = s
            self._last = s
        else:
            self._first = s
            self._last = s

    def find(self, i):
        current = self._first
        while current:
            if current.val == i:
                return True
            current = current.next
        return False

    def delete(self, i):
        found = False
        if self._first.val == i:
            found = True
            if self._first == self._last:
                self._first, self._last = None, None
            else:
                self._first = self._first.next
        else:
            current = self._first
            previous = None
            while current:
                if current.val == i:
                    found = True
                    if current == self._last:
                        self._last = previous
                        self._last.next = None
                        break
                    else:
                        previous.next = current.next
                        break
                previous = current
                current = current.next
        if not found:
            return False

    def delete_front(self):
        if self._first == self._last:
            self._first = None
            self._last = None
        else:
            self._first = self._first.next

    def delete_last(self):
        if self._first == self._last:
            self._first = None
            self._last = None
        else:
            current = self._first
            while current:
                if current.next == self._last:
                    self._last = current
                    current.next = None
                else:
                    current = current.next

    def is_empty(self):
        return self._first == None and self._last == None

