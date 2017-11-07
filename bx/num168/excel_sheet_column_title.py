class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ''
        while n:
            cha = chr(int((n-1) % 26 + 65))
            res += cha
            n = int((n-1) / 26)
        return res[::-1]
