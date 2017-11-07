#!/usr/bin/env python3
# coding: utf-8
# FileName: num189.py
# Author: lxw
# Date: 11/7/17 20:02:55 PM

"""
Num 189: Rotate Array
Source: https://leetcode.com/problems/rotate-array/description/

Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
"""

class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if k < 1 or length < 2:
            return
        _, k = divmod(k, length)
        nums[:] = nums[-k:] + nums[:-k]


def main():
    sol = Solution()
    nums = [1, 3, 2]
    sol.rotate(nums, 1)
    print(nums)


if __name__ == "__main__":
    main()