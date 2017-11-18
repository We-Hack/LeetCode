#!/usr/bin/env python3
# coding: utf-8
# FileName: num001.py
# Author: lxw
# Date: 20171105 7:18 PM

"""
Num 001: Two Sum
Source: https://leetcode.com/problems/two-sum/description/

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        Time: O(n) 39ms. Space: O(n).
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = {}
        for index, num in enumerate(nums):
            if target - num in nums_dict:
                return [nums_dict[target-num], index]
            else:
                nums_dict[num] = index


def main():
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], 9))


if __name__ == "__main__":
    main()
