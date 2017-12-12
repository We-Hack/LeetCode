#!/usr/bin/env python3
# coding: utf-8
# FileName: num121.py
# Author: lxw
# Date: 20171212 23:45:55 PM

"""
Num 121: Best Time to Buy and Sell Stock
Source: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.

"""

class Solution:
    # Method 1: DP. But really stupid and slow.
    def maxProfit_DP(self, prices):
        """
        Time: O(n) 115ms. Space: O(n).
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        if length <= 1:
            return 0
        left_min, right_max = prices[0], prices[-1]
        left_min_list = [left_min]
        right_max_list = [right_max]
        for i in range(1, length):
            left_min = min(left_min, prices[i])
            left_min_list.append(left_min)
            right_max = max(right_max, prices[-i-1])
            right_max_list.append(right_max)

        right_max_list = right_max_list[::-1]
        # print(left_min_list)
        # print(right_max_list)
        result = 0
        for i in range(length):
            result = max(right_max_list[i] - left_min_list[i], result)
        return result

    # Method 2:
    def maxProfit(self, prices):
        """
        Time: O(n) 82ms. Space: O(1).
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        if length <= 1:
            return 0

        current_min = prices[0]
        result = 0
        for i in range(length):
            if current_min > prices[i]:
                current_min = prices[i]
            else:
                result = max(result, prices[i]-current_min)
        return result

def main():
    sol = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    print(sol.maxProfit(prices))


if __name__ == "__main__":
    main()