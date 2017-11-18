#!/usr/bin/env python3
# coding: utf-8
# FileName: num461.py
# Author: lxw
# Date: 20171101 7:55 PM

"""
Num 461: Hamming Distance
Source: https://leetcode.com/problems/hamming-distance/description/
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different..
"""

class Solution(object):
    def hammingDistance(self, x, y):
        """
        # Time: O(1) 32ms. Space: O(1).
        :type x: int
        :type y: int
        :rtype: int
        """
        xor = x ^ y
        distance = 0
        while xor:
            if xor & 0x01:
                distance += 1
            xor = xor >> 1
        return distance


def main():
    sol = Solution()
    print(sol.hammingDistance(1, 4))
    print(sol.hammingDistance(1, 3))


if __name__ == "__main__":
    main()