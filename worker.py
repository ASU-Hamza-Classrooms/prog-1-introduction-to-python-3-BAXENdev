#!/bin/python3

from stringlib import *

#Add a Worker class to this file.
#
#The Worker class constructor needs to take as input
#a string.  It will set its own data member to that string.
#
#Add methods to the Worker class that are equivalent to
#functions in the stringlib module.  These methods will
#not take a string as input (except for the containsWord
#method, which will take the contained string parameter).  Instead,
#these methods will operate on the Worker class data member. 
#Your method can call the needed function in the stringlib
#module.

class Worker():
    def __init__(self, s: str) -> None:
        self.s = s

    def __str__(self) -> str:
        return f'Worker({self.s})'

    def __repr__(self) -> str:
        return f'Worker({self.s})'
    
    def reverseStr(self):
        return reverseStr(self.s)
    
    def containsWord(self, s: str):
        return containsWord(self.s, s)
    
    def isPalindrome(self):
        return isPalindrome(self.s)

    def upperCaseStr(self):
        return upperCaseStr(self.s)

