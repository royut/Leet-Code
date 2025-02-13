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
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        if not q and not p: return True
        if not q and p: return False
        if q and not p: return False
        if p.val != q.val:
            return False
        elif not p.left and not q.left and not q.right and not p.right:
            return True
        else:
            if (p.left and q.left) or (p.left == None and q.left == None):
                if not self.isSameTree(p.left, q.left):
                    return False
            else:
                return False
            if (p.right and q.right) or (p.right == None and q.right == None):
                if not self.isSameTree(p.right, q.right):
                    return False
            else:
                return False
        return True


if __name__ == '__main__':
    print('in main')
    p = TreeNode(1)
    q = TreeNode(1, None, TreeNode(2))
    print(Solution().isSameTree(p, q))
