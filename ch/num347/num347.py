#!/usr/bin/env python
# coding=utf-8
import collections
class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        return [item[0] for item in collections.Counter(nums).most_common(k)]
    #     nums = list(set(nums))
    #     length = len(nums)
    #     if k < 1 or k >length:
    #         return
    #     res = self.qsort(nums, 0, length-1)
    #     return res[:k]

    # def qsort(self, nums, left, right):
    #     if left >= right: return nums
    #     key = nums[left]
    #     lp = left
    #     rp = right
    #     while lp < rp:
    #         while nums[rp] >=key and lp < rp:
    #             rp -= 1
    #         while nums[lp] <= key and lp < rp:
    #             lp += 1
    #         nums[lp], nums[rp] = nums[rp], nums[lp]
    #     nums[left], nums[lp] = nums[lp], nums[left]
    #     self.qsort(nums, left, lp-1)
    #     self.qsort(nums, rp+1, right)
    #     return nums
        

if __name__ == '__main__':
    s = Solution()
    nums = [1,1,1,2,2,3]
    k = 2
    print(s.topKFrequent(nums, k))
