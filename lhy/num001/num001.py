class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_dict = {}
        for i in range(0,len(nums)):
            a = nums[i]
            b = target - a
            
            if  b in hash_dict:
                return [hash_dict[b],i]    
                
            hash_dict[a]=i
            
                
