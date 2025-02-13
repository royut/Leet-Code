# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    # def iter(self):
    #     current = self.left
    #     if self.left:


class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if root is None:
            return False
        stack = [root]
        while stack:
            node = stack.pop()
            print(node, node.val)
            if node.right:
                node.right.val = node.right.val + node.val
                stack.append(node.right)
            if node.left:
                node.left.val = node.left.val + node.val
                stack.append(node.left)
            if not node.left and not node.right and node.val == targetSum:
                return True
        return False


if __name__ == '__main__':
    q = TreeNode(1, TreeNode(10), TreeNode(20, None, TreeNode(7, None, None)))
    print(Solution().hasPathSum(q, 11))
