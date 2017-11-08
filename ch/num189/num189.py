import time
import random
class Solution1:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        k = k % len(nums)
        l = nums        
        """
        while k > 0:
            nums = [nums[-1]] + nums[:-1]
            k -= 1
        """
        for i in range(k):
            nums = [nums[-1]] + nums[:-1]
        l[:] = nums

class Solution2:
    def rotate(self, nums, k):
        k = k % len(nums)
        while k > 0:
            nums.insert(0, nums.pop())
            k -= 1

class Solution3:
    def rotate(self, nums, k):
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]


if __name__ == '__main__':
    s = Solution()
    l = [2,1,2]
    s.rotate(l, 1)
    print(l)
    """
    # nums = [i for i in range(1000)]
    nums = [random.randint(10, 1000) for i in range(1000)]
    l = nums
    l[:] = nums
    start_time = time.time()
    for _ in range(100000):
        nums[:] = [nums[-1]] + nums[:-1]
    end_time = time.time()
    print(end_time - start_time)

    nums[:] = l[:]
    start_time = time.time()
    for i in range(10000000):
        nums.insert(0, nums.pop())
    end_time = time.time()
    print(end_time - start_time)

    i = 0
    nums[:] = l[:]
    start_time = time.time()
    while i < 10000000:
        nums.insert(0, nums.pop())
        i += 1
    end_time = time.time()
    print(end_time - start_time)
    """


