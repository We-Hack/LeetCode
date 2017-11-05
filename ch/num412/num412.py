#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res_list = list()
        for i in range(1,n+1):
            if i % 15 == 0:
                res_list.append('FizzBuzz')
            else:
                if i % 5 == 0:
                    res_list.append('Buzz')
                elif i % 3 == 0:
                    res_list.append('Fizz')
                else:
                    res_list.append(str(i))
                    
        return res_list
