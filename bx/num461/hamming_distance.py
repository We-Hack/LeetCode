class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        a = x^y
        res = 0
        while a:
            res += 1
            a = a & (a-1)
        return res

