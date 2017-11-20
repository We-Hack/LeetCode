#!/usr/bin/env python3
# coding: utf-8
# FileName: num144.py
# Author: lxw
# Date: 20171120 14:22:55 PM

"""
Num 144: Binary Tree Preorder Traversal
Source: https://leetcode.com/problems/binary-tree-preorder-traversal/description/


Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],
   1
    \
     2
    /
   3
return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Iterative
class Solution:
    def preorderTraversal(self, root):
        """
        Time: 56 ms.
        :type root: TreeNode
        :rtype: List[int]
        """
        result, stack = [], []
        if not root:
            return result
        while 1:
            while root:
                result.append(root.val)
                stack.append(root)
                root = root.left
            if not stack:
                break
            node = stack.pop()
            root = node.right

        return result


'''
# Recursive
# Time: 72 ms
class Solution:
    def _preorder(self, root, result):
        if not root:
            return
        result.append(root.val)
        self._preorder(root.left, result)
        self._preorder(root.right, result)

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if not root:
            return result
        self._preorder(root, result)
        return result
'''


def main():
    sol = Solution()
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node1.right = node2
    node2.left = node3
    print(sol.preorderTraversal(node1))


if __name__ == "__main__":
    main()