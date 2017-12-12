#!/usr/bin/env python
# coding=utf-8
import math

class Solution:
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)

        if k > n*n or k < 0:
            return -1
        else:
            i = k // n
            j = k % n
        if j == 0:
            i -= 1
            j = n -1
        else:
            j -= 1
        return matrix[i][j]


if __name__ == '__main__':
    s = Solution()
    matrix = [
       [ 1,  5,  9],
       [10, 11, 13],
       [12, 13, 15]
    ]
    matrix = [[-5]]
    matrix = [[1,2],[1,3]]

    k = 2
    print(s.kthSmallest(matrix,k))