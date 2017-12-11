#!/usr/bin/env python3
# coding: utf-8
# FileName: num740.py
# Author: lxw
# Date: 20171211 7:55 PM

"""
Num 740: Delete and Earn
Source: https://leetcode.com/problems/delete-and-earn/description/

Given an array nums of integers, you can perform operations on the array.

In each operation, you pick any nums[i] and delete it to earn nums[i] points. After, you must delete every element equal to nums[i] - 1 or nums[i] + 1.

You start with 0 points. Return the maximum number of points you can earn by applying such operations.

Example 1:
Input: nums = [3, 4, 2]
Output: 6
Explanation: 
Delete 4 to earn 4 points, consequently 3 is also deleted.
Then, delete 2 to earn 2 points. 6 total points are earned.
Example 2:
Input: nums = [2, 2, 3, 3, 3, 4]
Output: 9
Explanation: 
Delete 3 to earn 3 points, deleting both 2's and the 4.
Then, delete 3 again to earn 3 points, and 3 again to earn 3 points.
9 total points are earned.
Note:

The length of nums is at most 20000.
Each element nums[i] is an integer in the range [1, 10000].
"""

from collections import Counter

# DP
class Solution:
    def deleteAndEarn(self, nums):
        """
        # Reference: https://discuss.leetcode.com/topic/112851/o-1-memory-7-lines-python
        Time: O(n), 66ms. Space: O(1).
        :type nums: List[int]
        :rtype: int
        counter = Counter(nums)
        if num in counter:
            counter[num]
        else:
            counter[num] == 0    # True
        """
        """
        f(n) = max(n * count(n) + f(n-2), f(n-1))
        f(n)表示<=n的数所能得到的最大得分(max score when using only numbers <= n)
        f(0) = 0, f(1) = count(1), f(2) = max(2 * count(2) + f(0), f(1))
        Since we only need the last 2 values of mx we can do it in O(1) space.(类似于递归实现的Fibonacci)
        """
        length = len(nums)
        if length < 1:
            return 0
        counter = Counter(nums)    # O(n)
        max_value = max(counter) + 1    # O(n)
        fn_2, fn_1 = 0, counter[1]
        for _index in range(2, max_value):  # O(n)
            fn_1, fn_2 = max(_index * counter[_index] + fn_2, fn_1), fn_1
        return fn_1


'''
# TLE
# Back-tracking
class Solution:
    def _back_tracking(self, nums_list, score_dict_temp, result_scores):
        if len(nums_list) == 0:
            score_sum = 0
            for score in score_dict_temp:
                score_sum += score * score_dict_temp[score]
            result_scores.append(score_sum)
            return

        process_set = set([])
        for _index, num in enumerate(nums_list):    # O(n^2)?
            if num in process_set:
                continue
            process_set.add(num)
            score_dict_temp[num] = score_dict_temp[num] if num in score_dict_temp else 0
            score_dict_temp[num] += 1
            temp_nums_list = nums_list[:_index] + nums_list[_index + 1:]
            temp_nums_list = [item for item in temp_nums_list if item +1 not in score_dict_temp and item - 1 not in score_dict_temp]
            self._back_tracking(temp_nums_list, score_dict_temp, result_scores)
            score_dict_temp[num] -= 1
            if score_dict_temp[num] == 0:
                del score_dict_temp[num]

    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result_scores = []
        self._back_tracking(nums, {}, result_scores)
        return max(result_scores)
'''


def main():
    sol = Solution()
    nums = [2, 2, 3, 3, 3, 4]    # 9
    # nums = [3, 4, 2]    # 6
    # nums = [8,3,4,7,6,6,9,2,5,8,2,4,9,5,9,1,5,7,1,4]      # TLE
    print(sol.deleteAndEarn(nums))


if __name__ == "__main__":
    main()