#!/usr/bin/env python3
# coding: utf-8
# File: num328.py
# Author: lxw
# Date: 20171120
"""
Num 328: Odd Even Linked List
Source: https://leetcode.com/problems/odd-even-linked-list/description/

Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.

Note:
The relative order inside both the even and odd groups should remain as it was in the input. 
The first node is considered odd, the second node even and so on ...

Credits:
Special thanks to @DjangoUnchained for adding this problem and creating all test cases.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def _show_linked_list(self, head):
        cur = head
        while cur:
            print(cur.val, end="->")
            cur = cur.next
        print("")

    def oddEvenList(self, head):
        """
        Time: O(n) 75 ms. Space: O(1).
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        cur = head
        odd_head = ListNode("odd")
        odd_cur = odd_head
        even_head = ListNode("even")
        even_cur = even_head
        odd_flag = True
        while cur:
            if odd_flag:
                odd_cur.next = cur
                odd_flag = False
                odd_cur = cur
            else:
                even_cur.next = cur
                odd_flag = True
                even_cur = cur
            cur = cur.next
        odd_cur.next = even_head.next
        even_cur.next = None    # This is essential
        head = odd_head.next
        return head


def main():
    sol = Solution()
    node1 = ListNode(1)
    node2 = ListNode(2)
    node1.next = node2
    node3 = ListNode(3)
    node2.next = node3
    sol._show_linked_list(node1)
    sol._show_linked_list(sol.oddEvenList(node1))

if __name__ == "__main__":
    main()
