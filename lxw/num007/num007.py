#!/usr/bin/env python3
# coding: utf-8
# FileName: num007.py
# Author: lxw
# Date: 11/6/17 9:58 PM

"""
Num 007: 
Source: https://leetcode.com/problems/reverse-integer/description/

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
Input: 123
Output:  321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range.
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""


class Solution:
    def reverse(self, x):
        """
        OK, but not good.
        Time: O(1) 122ms. Space: O(1).
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        INT_MAX = 2 ** 31
        INT_MIN = -INT_MAX    # INT_MIN: -2147483648
        INT_MAX -= 1    # INT_MAX: 2147483647
        if x == INT_MIN or x == INT_MAX:
            return 0

        sign = 1
        if x < 0:
            sign = -1
            x = -x

        result = 0
        while 1:
            quotient, mod = divmod(x, 10)
            result = result * 10 + mod
            if result > INT_MAX:
                return 0
            x = quotient
            if x == 0:
                break
        return sign * result

    def reverse_stupid(self, x):
        """
        Stupid and useless.
        Time: O(1) 156ms. Space: O(1).
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        sign = -1 if x < 0 else 1
        INT_MAX = 2 ** 31
        INT_MIN = -INT_MAX
        INT_MAX -= 1
        # print("INT_MIN:{}".format(INT_MIN))
        x_str = str(x)
        if sign == -1:
            x_str = x_str[1:]
        x_str = int(x_str[::-1]) * sign
        # print("x_str: {}".format(x_str))
        if x_str > INT_MAX or x_str < INT_MIN:
            return 0
        return x_str


def main():
    sol = Solution()
    print(sol.reverse(123))
    print(sol.reverse(-123))
    print(sol.reverse(120))
    print(sol.reverse(- (2 ** 31)))


if __name__ == "__main__":
    main()
