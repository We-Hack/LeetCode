class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0 
        if n == 1:
            return count
        else:
            for i in range(2, n):
                if self.isPrime(i):
                    count += 1
        return count

    def isPrime(self, n):
        for i in range(2, int(n/2+1)):
            if n % i == 0:
                return False
        return True



        

if __name__ == '__main__':
    s = Solution()
    print(s.countPrimes(4324423))