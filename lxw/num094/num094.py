#!/usr/bin/env python3
# coding: utf-8
# FileName: num094.py
# Author: lxw
# Date: 11/5/17 5:00 PM

"""
Num 094: Binary Tree Inorder Traversal
Source: https://leetcode.com/problems/binary-tree-inorder-traversal/description/
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],
   1
    \
     2
    /
   3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def _in_order_traveral(self, root, result):
        if not root:
            return
        self._in_order_traveral(root.left, result)
        result.append(root.val)        
        self._in_order_traveral(root.right, result)

    def inorderTraversal(self, root):
        """
        Time:
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self._in_order_traveral(root, result)
        return result



"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = []
        if not root:
            return result
        node = root
        while 1:
                        
            while node.left:                
                stack.append(node)
                node = node.left
            result.append(node.val)
            if node.right:
                node = node.right
            while len(stack) > 0:
                node = stack.pop()
                result.append(node.val)
                if node.right:
                    node = node.right
                    break
                
        return result
        
"""
        