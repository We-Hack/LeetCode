#!/usr/bin/env python3
# coding: utf-8
# File: num378.py
# Author: lxw
# Date: 20171119
"""
Num 378: Kth Smallest Element in a Sorted Matrix
Source: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/

Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note: 
You may assume k is always valid, 1 ≤ k ≤ n2.
"""


'''
# TLE
class Solution:
    def _quick_sort(self, nums):
        if nums:
            return self._quick_sort([item for item in nums[1:] if item <= nums[0]]) + nums[:1] + self._quick_sort([item for item in nums[1:] if item > nums[0]])
        return []

    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        one_dimension_matrix = [item for row in matrix for item in row]
        one_dimension_matrix = self._quick_sort(one_dimension_matrix)
        return one_dimension_matrix[k-1]
'''
class Solution:
    def kthSmallest(self, matrix, k):
        """
        Time: O(2n^2logn) 109ms. Space: O(n^2)
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        one_dimension_matrix = [item for row in matrix for item in row]
        one_dimension_matrix.sort()
        return one_dimension_matrix[k-1]


def main():
    sol = Solution()
    matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    k = 8
    print(sol.kthSmallest(matrix, k))

if __name__ == "__main__":
    main()
