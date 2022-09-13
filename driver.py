#!/bin/python3

#import the code in string1.py

from stringlib import *
from worker import *
import sys

#Function to test the functions in the stringlib module
def testStringLib(inputStr):
    s = inputStr
    print(f's = {s}')
    print(f'Reverse s = {reverseStr(s)}')
    print(f'Does s contain "are"? {containsWord(s, "are")}')
    print(f'Is s a pailindrome? {isPalindrome(s)}')
    print(f'Upper case s = {upperCaseStr(s)}')
    return

#Function to test the methods in the Worker class in the worker module
def testWorkerClass(inputStr):
    w = Worker(inputStr)
    print(f'w = {w}')
    print(f'Reverse w = {w.reverseStr()}')
    print(f'Does w contain "ple"? {w.containsWord("ple")}')
    print(f'Is w a palindrome? {w.isPalindrome()}')
    print(f'Upper case w = {w.upperCaseStr()}')
    return

#check to make sure there is a string command line argument
if (len(sys.argv) < 2):
    print("usage: driver1.py <string>")
else:
    #call the functions that test the library and the Worker class
    print("\nTest stringlib:")
    testStringLib(sys.argv[1])
    print("\nTest Worker class:")
    testWorkerClass(sys.argv[1])




