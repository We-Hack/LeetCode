#!/usr/bin/env python3
# coding: utf-8
# File: num384.py
# Author: lxw
# Date: 20171118
"""
Num 384: Shuffle an Array
Source: https://leetcode.com/problems/shuffle-an-array/description/

Shuffle a set of numbers without duplicates.

Example:

// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();
"""

import random

# Method 5
# Reference: https://discuss.leetcode.com/topic/54136/easy-python-solution-based-on-generating-random-index-and-swapping
class Solution:
    """
    Time: 672 ms. Good. Be careful.
    """
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        result = self.nums[:]
        length = len(result) - 1
        for i in range(length):
            j = random.randint(i, length)    # NOTE(Be careful): MUST be random.randint(i, length), NOT random.randint(i+1, length), 因为可能不用交换, 如果是(i+1, length) 则表示一定会交换
            result[i], result[j] = result[j], result[i]
        return result

'''
# Method 4
# Reference: https://discuss.leetcode.com/topic/54136/easy-python-solution-based-on-generating-random-index-and-swapping
class Solution:
    """
    # Time: 778ms.
    这种方法:[缺点]每次shuffle是基于上一次shuffle的结果进行的修改，而不是基于原来的nums的修改。
    [优点]空间复杂度比Method5要好，不用每次shuffle都重新生成一个新的nums。
    但从全局的情况来看（重复调用shuffle多次的整体结果)应该和Method5是一致的。
    """
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.origin_nums = nums[:]
        self.nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.origin_nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        length = len(self.nums) - 1
        for i in range(length):
            j = random.randint(i, length)    # NOTE(Be careful): MUST be random.randint(i, length), NOT random.randint(i+1, length), 因为可能不用交换, 如果是(i+1, length) 则表示一定会交换
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        return self.nums
'''

'''
# Method 3
class Solution:
    """
    The same as Method 2.
    Time: 898 ms. Slow.
    """
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        return random.sample(self.nums, len(self.nums))
'''

'''
# Method 2
class Solution:
    """
    Time: 866 ms. Concise but slow.
    """
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.reset = lambda : nums
        self.shuffle = lambda : random.sample(nums, len(nums))
'''

'''
# Method 1
class Solution:
    """
    Time: 825 ms. Bad
    """
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        length = len(self.nums)
        index_list = [index for index in range(length)]
        shuffle_list = []
        while length > 0:
            length -= 1
            index_list_index = random.randint(0, length)
            shuffle_list.append(self.nums[index_list[index_list_index]])
            del index_list[index_list_index]

        return shuffle_list
'''

def main():
    nums = [1, 2, 3]
    sol = Solution(nums)
    print(sol.shuffle())   # Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
    sol.reset() # Resets the array back to its original configuration [1,2,3].
    print(sol.shuffle())   # Returns the random shuffling of array [1,2,3].


if __name__ == "__main__":
    main()
