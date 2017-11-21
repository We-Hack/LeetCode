#!/usr/bin/env python3
# coding: utf-8
# FileName: num145.py
# Author: lxw
# Date: 20171121 23:33:55 PM

"""
Num 145: Binary Tree Postorder Traversal
Source: https://leetcode.com/problems/binary-tree-postorder-traversal/

Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [3,2,1].

Note: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Iterative
# Time: O(n) 66ms. Space: O(n).
class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result, stack = [], []
        while 1:
            while root:
                stack.append((root, 0))
                root = root.left
            if not stack:
                break
            node, flag = stack.pop()
            if flag == 0:    # left is already traversed.
                stack.append((node, 1))
                root = node.right
            else:    # right is already traversed.
                result.append(node.val)

        return result


'''
# Recursive
# Time: 62 ms
class Solution:
    def _postorder(self, root, result):
        if not root:
            return
        self._postorder(root.left, result)
        self._postorder(root.right, result)
        result.append(root.val)

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self._postorder(root, result)
        return result
'''


def main():
    sol = Solution()
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node1.right = node2
    node2.left = node3
    print(sol.postorderTraversal(node1))


if __name__ == "__main__":
    main()