#!/usr/bin/env python3
# coding: utf-8
# FileName: num022.py
# Author: lxw
# Date: 20171119 16:23 PM

"""
Num 022: Generate Parentheses
Source: https://leetcode.com/problems/generate-parentheses/description/

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""
import pprint

class Solution:
    def _parenthesis(self, n, left, right, result, result_list):
        if left == n and right == n:
            result_list.append(result)
            return
        if left < n:
            result_left = result[:]
            result_left.append("(")
            self._parenthesis(n, left+1, right, result_left, result_list)
        if right < n:
            length = left + right
            if length & 0x01 == 1:    # odd
                length += 1
            if right < (length >> 1):
                result_right = result[:]
                result_right.append(")")
                self._parenthesis(n, left, right+1, result_right, result_list)

    def generateParenthesis(self, n):
        """
        Recursive.
        Time: 59 ms
        :type n: int
        :rtype: List[str]
        """
        result_list = []
        self._parenthesis(n, 0, 0, [], result_list)
        result_list = ["".join(parenthesis_list) for parenthesis_list in result_list]
        return result_list


def main():
    sol = Solution()
    pprint.pprint(sol.generateParenthesis(3))


if __name__ == "__main__":
    main()
