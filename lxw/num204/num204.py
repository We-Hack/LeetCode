#!/usr/bin/env python3
# coding: utf-8
# FileName: num204.py
# Author: lxw
# Date: 20171105 7:20 PM

"""
Num 204: Count Primes
Source: https://leetcode.com/problems/count-primes/description/

Count the number of prime numbers less than a non-negative number, n.

Credits:
Special thanks to @mithmatt for adding this problem and creating all test cases.
"""


import math


class Solution(object):
    def _is_prime_bad2(self, n):
        """
        # Better than _is_prime_bad1 but still bad.
        # Reference: [判断一个数是否为质数/素数——从普通判断算法到高效判断算法思路](blog.csdn.net/huang_miao_xin/article/details/51331710)
        令x≥1，将大于等于5的自然数表示如下：
        6x-1, 6x, 6x+1, 6x+2, 6x+3, 6x+4, 6x+5, 6(x+1), 6(x+1)+1 ···
        可以看到，不在6的倍数两侧，即6x两侧的数为6x+2，6x+3，6x+4，由于2(3x+1)，3(2x+1)，2(3x+2)，所以它们一定不是素数，再除去6x本身，显然，素数要出现只可能出现在6x的相邻两侧。
        任何一个合数都可以分解为几个质数的积
        :param n: 
        :return: 
        """
        if n == 2 or n == 3:
            return True
        if n % 6 != 1 and n % 6 != 5:
            return False
        sqrt_n = int(math.sqrt(n)) + 1
        index = 5
        while index < sqrt_n:
            if n % index == 0 or n % (index + 2) == 0:
                return False
            index += 6
        return True

    def _is_prime_bad1(self, n):
        """
        Bad: Time Limit Exceeded.
        """
        sqrt_n = int(math.sqrt(n)) + 1
        for i in range(2, sqrt_n):
            if n % i == 0:
                return False
        return True

    def countPrimes_bad(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for i in range(2, n):
            if self._is_prime_bad1(i):
            # if self._is_prime_bad2(i):
                count += 1
        return count

    def countPrimes(self, n):
        """
        Time: 446 ms. beats 79%. How could be better and faster?
        :param n: 
        :return: 
        """
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
        return sum(primes)


def main():
    sol = Solution()
    print(sol.countPrimes(10))


if __name__ == "__main__":
    main()