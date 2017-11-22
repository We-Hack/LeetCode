#!/usr/bin/env python3
# coding: utf-8
# File: num350.py
# Author: lxw
# Date: 20171122 09:32 AM
"""
Num 350: Intersection of Two Arrays II
Source: https://leetcode.com/problems/intersection-of-two-arrays-ii/description/

Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""

import collections


'''
# Method1
class Solution:
    def intersect(self, nums1, nums2):
        """
        Time: O(m+n) 59ms. Space: O(m+n).
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        if not nums1 or not nums2:
            return result
        nums1_count = collections.Counter(nums1)    # A Counter is a dict subclass for counting hashable objects.
        nums2_count = collections.Counter(nums2)
        for key in nums1_count:
            if key in nums2_count:
                result.extend([key] * min(nums1_count[key], nums2_count[key]))

        return result
'''

# Method2
class Solution:
    def intersect(self, nums1, nums2):
        """
        Time: O(m+n) 56ms. Space: O(m+n).
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        if not nums1 or not nums2:
            return result
        nums1_count = {}
        for num in nums1:
            nums1_count[num] = nums1_count.setdefault(num, 0) + 1
        nums2_count = {}
        for num in nums2:
            nums2_count[num] = nums2_count.setdefault(num, 0) + 1
        for key in nums1_count:
            if key in nums2_count:
                result.extend([key] * min(nums1_count[key], nums2_count[key]))
        return result


def main():
    sol = Solution()
    nums1 = [1, 2, 2, 1, 3]
    nums2 = [2, 2, 5, 2, 3]
    print(sol.intersect(nums1, nums2))

if __name__ == "__main__":
    main()
