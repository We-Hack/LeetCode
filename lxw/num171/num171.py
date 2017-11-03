#!/usr/bin/env python3
# coding: utf-8
# FileName: num171.py
# Author: lxw
# Date: 11/3/17 14:02:55 PM

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

class Solution(object):
    def titleToNumber(self, s):
        """
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


def main():
    sol = Solution()
    print(sol.titleToNumber("B"))
    print(sol.titleToNumber("BA"))


if __name__ == "__main__":
    main()