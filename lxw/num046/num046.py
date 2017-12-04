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
    '''
    # Method1.1 vs Method1.2: 1.2更好，虽然1.1的执行时间短，但1.1空间复杂度高，算法思想不够直观。
    def _permuation(self, nums, permutation, remainder_index_list, result_list):
        if len(remainder_index_list) == 0:
            result_list.append(permutation)
            return

        for _index, num_index in enumerate(remainder_index_list):
            _permutation = permutation[:]
            _permutation.append(nums[num_index])
            self._permuation(nums, _permutation, remainder_index_list[:_index] + remainder_index_list[_index+1:], result_list)


    # Method 1.1: Recursive
    def permute(self, nums):
        """
        Time: 86ms.
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
    '''
    def _permutation(self, result_list, permutation, remainders):
        """
        :param result_list: 
        :param permutation: 
        :param remainders: 
        :return: 
        """
        if len(remainders) == 0:
            result_list.append(permutation[:])
            return
        for _index, item in enumerate(remainders):
            permutation.append(item)
            self._permutation(result_list, permutation, remainders[:_index] + remainders[_index+1:])
            permutation.pop()    # 回溯的体现


    # Method 1.2: Recursive
    def permute(self, nums):
        """
        Time: 106ms.
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        if length < 2:
            return [nums]
        result_list = []
        self._permutation(result_list, [], nums)
        return result_list

    # Method 2: Iterative (https://discuss.leetcode.com/topic/6377/my-ac-simple-iterative-java-python-solution)
    def permute_2(self, nums):
        """
        Time: 79ms.
        Time Cost: O(1! + 2! + 3! + ... + n!)
        Space Cost: O(1! + 2! + 3! + ... + n!)
        """
        # Idea: to permute n numbers, we can add the nth number into the resulting List<List<Integer>> from the n-1 numbers, in every possible position.
        perms = [[]]
        for n in nums:
            temp_perms = []
            length = len(perms[0]) + 1
            for perm in perms:
                for i in range(length):
                    temp_perms.append(perm[:i] + [n] + perm[i:])   ###insert n
            perms = temp_perms
        return perms


def main():
    sol = Solution()
    nums = [1, 2, 3]
    pprint.pprint(sol.permute(nums))
    pprint.pprint(sol.permute_2(nums))


if __name__ == "__main__":
    main()
