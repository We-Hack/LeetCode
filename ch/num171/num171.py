class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return ord(s) - 64
        else:
            res = self.titleToNumber(s[1:]) + 26 ** (len(s)-1) * (ord(s[0])-64)
            # print(res)
            s = s[1:]
            return res



if __name__ == '__main__':
    s = Solution()
    a = s.titleToNumber('AAA')
    print(a)