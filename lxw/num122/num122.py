#!/usr/bin/env python3
# coding: utf-8
# FileName: num122.py
# Author: lxw
# Date: 20171213 11:42:55 AM

"""
Num 122: Best Time to Buy and Sell Stock II
Source: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like
(ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple
transactions at the same time (ie, you must sell the stock before you buy again).
"""

class Solution:
    # Method 1: 这种算法虽然有点儿投机取巧，但其实有很简单，但不太容易发现的思想(a, b, c:  b - a + c - b = c - a).
    # 这种方法的缺点的在同一天中存在买和卖的情况(如果不允许在同一天买和卖，就不能用这种方法)
    def maxProfit_1(self, prices):
        """
        Time: O(n) 62ms. Space: O(1).
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        if length < 2:
            return 0
        result = 0
        length -= 1
        for _index in range(length):
            if prices[_index+1] > prices[_index]:
                result += prices[_index+1] - prices[_index]
        return result

    # Method 2: 查找局部最小值和局部最大值(人的直观思维模式: 可以把问题，应用到真实的场景中，解题方法自然就出来了)
    def maxProfit(self, prices):
        """
        Time: O(n) 62ms. Space: O(1).
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        if length < 2:
            return 0
        i = 0
        length -= 1
        result = 0
        while i < length:
            # Find the local minimum.
            while i < length:
                if prices[i+1] <= prices[i]:
                    i += 1
                else:
                    break
            start = i

            # Find the local maximum.
            while i < length:
                if prices[i+1] >= prices[i]:
                    i += 1
                else:
                    break
            end = i
            result += prices[end] - prices[start]
        return result



def main():
    sol = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    print(sol.maxProfit(prices))


if __name__ == "__main__":
    main()