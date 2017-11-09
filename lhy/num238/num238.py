class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        output = [1] * length
        
        left = 1
        for index in range(length-1):
            left*= nums[index]
            output[index+1]*=left
            
        right = 1
        for index in range(length-1, 0, -1):
            right *= nums[index]
            output[index-1]*=right
            
        return output
