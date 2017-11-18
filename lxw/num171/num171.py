#!/usr/bin/env python3
# coding: utf-8
# FileName: num171.py
# Author: lxw
# Date: 20171103 14:02:55 PM

"""
Num 171: Excel Sheet Column Number
Source: https://leetcode.com/problems/excel-sheet-column-number/description/

Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
Credits:
Special thanks to @ts for adding this problem and creating all test cases.
"""


from functools import reduce


class Solution(object):
    def titleToNumber_method1(self, s):
        """
        Time: O(n). Space: O(1).
        :type s: str
        :rtype: int
        """
        BASE = 26
        char_dict = {chr(ch): ch-64  for ch in range(65, 91)}
        result = 0
        for ch in s:
            result *= BASE
            result += char_dict[ch]

        return result

    def titleToNumber_method2(self, s):
        """
        Beautiful
        Time: O(n). Space: O(1).
        :type s: str
        :rtype: int
        """
        return reduce(lambda x, y: 26*x+y, [ord(ch)-64 for ch in s])

def main():
    sol = Solution()
    print(sol.titleToNumber_method1("B"))
    print(sol.titleToNumber_method2("B"))
    print(sol.titleToNumber_method1("BA"))
    print(sol.titleToNumber_method2("BA"))


if __name__ == "__main__":
    main()