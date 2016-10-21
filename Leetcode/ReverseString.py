# https://leetcode.com/problems/reverse-string/
#Write a function that takes a string as input and returns the string reversed.
#
#Example:
#Given s = "hello", return "olleh".

#ref: http://stackoverflow.com/questions/3705670/best-way-to-create-a-reversed-list-in-python

# This is an elegant way of list slicing
def ReverseString(s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]

# This solution is faster
def ReverseString2(s):
        """
        :type s: str
        :rtype: str
        """
        # note that reversed() returns an iterator
        return ''.join(reversed(s))