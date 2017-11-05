class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        buff_dict = {}
        if not nums:
            return False
        for index, num in enumerate(nums):
            if num in buff_dict:
                return [buff_dict[num], index]
            else:
                buff_dict[target-num] = index
        
        
        
if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2,7, 11, 16], 9))