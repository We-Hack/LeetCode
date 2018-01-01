#!/usr/bin/env python3
# coding: utf-8
# FileName: num072.py
# Author: lxw
# Date: 20180101 18:00 PM

"""
Num 072: Edit Distance
Source: https://leetcode.com/problems/edit-distance/description/

Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character
"""
"""
[Levenshtein distance symmetric?](https://stackoverflow.com/questions/9722022/levenshtein-distance-symmetric)
Just looking at the basic algorithm it definitely is symmetric given the same cost for the operations - the number of additions, deletions and substitutions to get from a word A to a word B is the same as getting from word B to word A.

If there is a different cost on any of the operations there can be a difference though, e.g. if addition has a cost of 2 and deletion a cost of 1 to get from Zombie to Zombies results in a distance of 2, the other way round would be 1 - not symmetric.
"""

import copy
import pprint


# Improvement: https://leetcode.com/problems/edit-distance/discuss/25879

class Solution:
    def minDistance(self, word1, word2):
        """
        Time: O(len1 * len2) 515ms. Space: O(len1 * len2)
        :type word1: str
        :type word2: str
        :rtype: int
        """
        len1 = len(word1)
        len2 = len(word2)
        if len1 == 0:
            return len2
        elif len2 == 0:
            return len1

        DEL_COST = 1
        INS_COST = 1
        SUB_COST = 1
        len1 += 1
        len2 += 1
        # array_1d = [i for i in range(len2)]    # Initialization
        # array_2d = [copy.deepcopy(array_1d) for i in range(len1)]
        array_2d = [[i for i in range(len2)] for i in range(len1)]    # Initialization
        for i in range(len1):    # Initialization
            array_2d[i][0] = i

        # Recurrence
        for i in range(1, len1):
            for j in range(1, len2):
                ins_del = min(array_2d[i-1][j] + DEL_COST, array_2d[i][j-1] + INS_COST)
                sub = array_2d[i-1][j-1]
                sub += SUB_COST if word1[i-1] != word2[j-1] else 0
                array_2d[i][j] = min(sub, ins_del)

        # Termination
        # pprint.pprint(array_2d)
        return array_2d[len1-1][len2-1]


def main():
    sol = Solution()
    word1, word2 = "intention", "execution"
    print("Edit Distance(\"{0}\", \"{1}\"): {2}".format(word1, word2, sol.minDistance(word1, word2)))
    word1, word2 = "execution", "intention"
    print("Edit Distance(\"{0}\", \"{1}\"): {2}".format(word1, word2, sol.minDistance(word1, word2)))
    word1, word2 = "iloveu", "hello"
    print("Edit Distance(\"{0}\", \"{1}\"): {2}".format(word1, word2, sol.minDistance(word1, word2)))
    word1, word2 = "hello", "iloveu"
    print("Edit Distance(\"{0}\", \"{1}\"): {2}".format(word1, word2, sol.minDistance(word1, word2)))
    word1, word2 = "a", "a"
    print("Edit Distance(\"{0}\", \"{1}\"): {2}".format(word1, word2, sol.minDistance(word1, word2)))


if __name__ == "__main__":
    main()
