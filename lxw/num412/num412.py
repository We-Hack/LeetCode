#!/usr/bin/env python3
# coding: utf-8
# FileName: num412.py
# Author: lxw
# Date: 20171110 9:15 PM

"""
Num 412: Fizz Buzz
Source: https://leetcode.com/problems/fizz-buzz/description/

Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
"""

class Solution(object):
    def fizzBuzz_method1(self, n):
        """
        OK. Time: O(n) "%" is slow. Space: O(1)
        :type n: int
        :rtype: List[str]
        """
        result = []
        for i in range(1, n+1):
            mod3 = i % 3
            mod5 = i % 5
            if mod3 == 0 and mod5 == 0:
                result.append("FizzBuzz")
            elif mod3 == 0:
                result.append("Fizz")
            elif mod5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result

    def fizzBuzz_method2(self, n):
        """
        Better. Time: O(n) w/o "%". Space: O(1)
        :type n: int
        :rtype: List[str]
        """
        result = []
        sum3, sum5 = 0, 0
        for i in range(n):
            sum3 += 1
            sum5 += 1
            if sum3 == 3 and sum5 == 5:
                result.append("FizzBuzz")
                sum3, sum5 = 0, 0
            elif sum3 == 3:
                result.append("Fizz")
                sum3 = 0
            elif sum5 == 5:
                result.append("Buzz")
                sum5 = 0
            else:
                result.append(str(i+1))
        return result

def main():
    sol = Solution()
    print(sol.fizzBuzz_method1(15))
    print(sol.fizzBuzz_method2(15))


if __name__ == "__main__":
    main()