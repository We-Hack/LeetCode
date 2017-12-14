#!/usr/bin/env python3
# coding: utf-8
# FileName: num744.py
# Author: lxw
# Date: 20171214 15:24 PM

"""
Num 744: Find Smallest Letter Greater Than Target
Source: https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/

Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, find the smallest element in the list that is larger than the given target.

Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.

Examples:
Input:
letters = ["c", "f", "j"]
target = "a"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "c"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "d"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "g"
Output: "j"

Input:
letters = ["c", "f", "j"]
target = "j"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "k"
Output: "c"
Note:
letters has a length in range [2, 10000].
letters consists of lowercase letters, and contains at least 2 unique letters.
target is a lowercase letter.
"""


class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        Time: O(logn) 62ms. Space: O(1).
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        if target < letters[0] or target >= letters[-1]:
            return letters[0]
        start = 0
        end = len(letters) - 1
        while start <= end:
            mid = (start + end) >> 1
            if letters[mid] > target:
                end = mid - 1
            elif letters[mid] <= target:
                start = mid + 1
        return letters[start]
