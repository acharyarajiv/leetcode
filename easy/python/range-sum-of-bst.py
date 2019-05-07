'''
This can be solved using ay recursive traversal method
which could be a better solution than the below
too lazy to write recursion after implementing BST
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        res = 0
        stack = []
        stack.append(root)
        while len(stack) > 0:
            node = stack.pop()
            if node.val >= L and node.val <= R:
                res += node.val
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
        return res


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BST(object):
    def __init__(self):
        self.root = None

    def __findAndInsert__(self, root, val):
        if root is None:
            root = TreeNode(val)
        elif root.val > val:
            root.left = self.__findAndInsert__(root.left, val)
        else:
            root.right = self.__findAndInsert__(root.right, val)
        return root

    def __printNodes__(self, root):
        if root is not None:
            print(root.val)
            self.__printNodes__(root.left)
            self.__printNodes__(root.right)

    def insert(self, val):
        root = self.root
        self.root = self.__findAndInsert__(root, val)

    def printTree(self):
        self.__printNodes__(self.root)


if __name__ == '__main__':
    inp_arr = [[[10,5,15,3,7,None,18], 7, 15],
            [[10,5,15,3,7,13,18,1, None,6], 6, 10]]
    out_arr = [32, 23]
    s = Solution()
    for index, value in enumerate(inp_arr):
        root_arr = value[0]
        bst = BST()
        for val in root_arr:
            bst.insert(val)
        res = s.rangeSumBST(bst.root, value[1], value[2])
        print('Input %s, left %d, right %d' % (value[0], value[1], value[2]))
        print('Output\nExpected %d\nActual %d\n' % (out_arr[index], res))
