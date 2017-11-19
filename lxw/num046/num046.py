#!/usr/bin/env python3
# coding: utf-8
# FileName: num046.py
# Author: lxw
# Date: 20171119 17:13 PM

"""
Num 046: Permutations
Source: https://leetcode.com/problems/permutations/description/

Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

import pprint

class Solution:
    def _permuation(self, nums, permutation, remainder_index_list, result_list):
        if len(remainder_index_list) == 0:
            result_list.append(permutation)
            return

        for _index, num_index in enumerate(remainder_index_list):
            _permutation = permutation[:]
            _permutation.append(nums[num_index])
            self._permuation(nums, _permutation, remainder_index_list[:_index] + remainder_index_list[_index+1:], result_list)


    def permute(self, nums):
        """
        Time: 96ms.
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        if length < 2:
            return [nums]
        result_list = []
        permutation = []
        remainder_index_list = [_index for _index in range(length)]
        self._permuation(nums, permutation, remainder_index_list, result_list)
        return result_list


def main():
    sol = Solution()
    nums = [1, 2, 3]
    pprint.pprint(sol.permute(nums))


if __name__ == "__main__":
    main()
