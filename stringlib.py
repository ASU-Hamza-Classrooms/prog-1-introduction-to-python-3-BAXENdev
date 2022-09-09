#!/bin/python3

#Add the following functions:
#
#reverseStr - takes as input a string and returns the reverse of it
def reverseStr(s: str):
    return s[::-1]

#
#containsWord - takes as input two strings, containingStr and containedStr,
#and returns "Yes" if containedStr is anywhere within containingStr 
#and returns "No" otherwise
def containsWord(containingStr: str, containedStr: str):
    return "Yes" if containedStr in containingStr else "No"

#
#isPalindrome - takes as input a string and returns "Yes" if it is
#palindrome and "No" otherwise  
def isPalindrome(s: str):
    r = reverseStr(s)
    return "Yes" if r == s else "No"

#
#upperCaseStr - takes as input a string and returns the identical string
#with the characters 'a' ... 'z' changed to uppercase
#
def upperCaseStr(s: str):
    return s.upper()


