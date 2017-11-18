# coding:utf-8
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# res = []

class Solution1:
    # recursively
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # if not root:
        #     return
        # print(root.val)
        # res.append(root.val)
        # self.inorderTraversal(root.left)
        # self.inorderTraversal(root.right)
        res = []
        self.helper(root, res)
        return res


    def helper(self, root, res):
        if root:
            self.helper(root.left, res)
            res.append(root.val)
            self.helper(root.right, res)


class Solution2:
    # recursively
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # res = list()
        # stack = list()
        # p = root
        # while p or stack:
        #     while p:
        #         stack.append(p)
        #         p = p.left
        #     if stack:
        #         p = stack.pop()
        #         res.append(p.val)
        #         p = p.right
        res = list()
        stack = list()
        p = root
        while p or stack:
            while p:
                stack.append(p)
                p = p.left
            if stack:

                p = stack.pop()
                res.append(p.val)
                p = p.right
        return res


if __name__ == '__main__':
    s2= Solution2()
    s1 = Solution1()
    root = TreeNode('G')
    l2_1  = TreeNode("D")
    l2_2 = TreeNode("M")
    l3_1 = TreeNode("A")
    l3_2 = TreeNode("E")
    l3_3 = TreeNode('H')
    l3_4= TreeNode('Z')
    l4_1 = TreeNode('F')

    root.left = l2_1
    root.right = l2_2
    l2_1.left = l3_1
    l2_1.right = l3_2
    l2_2.right = l3_4
    l2_2.left = l3_3
    l3_2.left = l4_1
    res = s1.inorderTraversal(root)
    print(res)
    res = s2.inorderTraversal(root)
    print(res)