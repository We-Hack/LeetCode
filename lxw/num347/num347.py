#!/usr/bin/env python3
# coding: utf-8
# File: num347.py
# Author: lxw
# Date: 20171109
"""
Num 347: Top K Frequent Elements
Source: https://leetcode.com/problems/top-k-frequent-elements/description/

Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note: 
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""


import collections


class Solution:
    def _quick_sort(self, nums):
        if not nums:
            return []
        return self._quick_sort([num for num in nums[1:] if num < nums[0]]) + nums[:1] + self._quick_sort([num for num in nums[1:] if num >= nums[0]])
        
    def topKFrequent_slow(self, nums, k):
        """
        Time: O(nlogn). 118ms. Space: O(n).
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        index, length = 1, len(nums)
        if length < 1:
            return []

        # nums = self._quick_sort(nums)     # 395ms.
        nums.sort()    # 118ms.
        num_count_dic = {}
        last_num = nums[0]
        count = 1
        while index < length:
            if nums[index] == last_num:
                count += 1
            else:
                num_count_dic[last_num] = count
                count = 1
                last_num = nums[index]
            index += 1
        num_count_dic[last_num] = count
        # print(num_count_dic)
        sorted_key = sorted(num_count_dic, key=lambda x:num_count_dic[x], reverse=True)
        return sorted_key[:k]

    def topKFrequent(self, nums, k):
        """
        Time: O(nlogn). 89ms. Space: O(n).
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        length = len(nums)
        if length < 1:
            return []
        num_count_dic = collections.Counter(nums)
        return sorted(num_count_dic, key=lambda x:num_count_dic[x], reverse=True)[:k]


def main():
    sol = Solution()
    nums = [2, 1, 2, 3, 2, 3, 2]
    # nums = [2, 1, -2]
    print(nums)
    print(sol.topKFrequent(nums, 2))

if __name__ == "__main__":
    main()
