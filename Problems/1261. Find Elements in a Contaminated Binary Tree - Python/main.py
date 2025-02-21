# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindElements(object):
    vals = set()

    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        root.val = 0
        self.vals = set()
        self.vals.add(root.val)
        stack = [root]
        while stack:
            current = stack.pop()
            if current.left:
                stack.append(current.left)
                current.left.val = 2 * current.val + 1
                self.vals.add(current.left.val)
            if current.right:
                stack.append(current.right)
                current.right.val = 2 * current.val + 2
                self.vals.add(current.right.val)

    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        if target in self.vals:
            return True
        return False


if __name__ == '__main__':
    print('in main')
    root = TreeNode(-1, None, TreeNode(-1, TreeNode(-1, TreeNode(-1))))
    # Your FindElements object will be instantiated and called as such:
    obj = FindElements(root)
    print(obj.find(2))
    print(obj.find(3))
    print(obj.find(4))
    print(obj.find(5))