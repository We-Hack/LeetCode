#!/usr/bin/env python
# coding=utf-8

class Solution1:
    def productExceptSelf(self, nums):
        """
        inputted:type: nums List[int]
        inputted:rtype: List[int]
        inputted"""
        result = list()
        for index, num in enumerate(nums):
            s = 1
            for i,k in enumerate(nums):
                if i == index:
                    continue
                s = s * k
            result.append(s)
        return result


class Solution2:
    def productExceptSelf(self, nums):
        p = 1
        n = len(nums)
        output = []
        for i in range(0,n):
            output.append(p)
            p = p * nums[i]
        p = 1
        for i in range(n-1,-1,-1):
            output[i] = output[i] * p
            p = p * nums[i]
        return output


        
        
        




if __name__ == '__main__':
    s = Solution2()
    nums = [1,2,3,4]
    
    print(s.productExceptSelf(nums))
