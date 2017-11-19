#!/usr/bin/env python3
# coding: utf-8
# FileName: num287.py
# Author: lxw
# Date: 20171129 00:56 AM

"""
Num 287: Find the Duplicate Number
Source: https://leetcode.com/problems/find-the-duplicate-number/description/

Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
"""

# Reference: https://discuss.leetcode.com/topic/31011/python-same-solution-as-142-linked-list-cycle-ii

class Solution:
    def findDuplicate(self, nums):
        """
        Time: O(n) 62ms. Space: O(1).
        :type nums: List[int]
        :rtype: int
        """
        slow = fast = finder = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                while finder != slow:
                    finder = nums[finder]
                    slow = nums[slow]
                return finder

