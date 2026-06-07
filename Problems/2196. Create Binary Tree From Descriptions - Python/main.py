# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def createBinaryTree(self, descriptions):
        """
        :type descriptions: List[List[int]]
        :rtype: Optional[TreeNode]
        """
        val_to_node = {}
        children = set()
        for p, c, d in descriptions:
            if p not in val_to_node:
                val_to_node[p] = TreeNode(p)
            if c not in val_to_node:
                val_to_node[c] = TreeNode(c)
            if d == 1:
                val_to_node[p].left = val_to_node[c]
            else:
                val_to_node[p].right = val_to_node[c]
            children.add(c)
        for node in val_to_node:
            if node not in children:
                return val_to_node[node]


if __name__ == "__main__":
    print('in main')
    # descriptions = [[20, 15, 1], [20, 17, 0], [50, 20, 1], [50, 80, 0], [80, 19, 1]]
    # descriptions = [[1, 2, 1], [2, 3, 0], [3, 4, 1]]
    # descriptions = [[85, 82, 1], [74, 85, 1], [39, 70, 0], [82, 38, 1], [74, 39, 0], [39, 13, 1]]
    descriptions = [[39, 70, 1], [13, 39, 1], [85, 74, 1], [74, 13, 1], [38, 82, 1], [82, 85, 1]]
    tree = (Solution().createBinaryTree(descriptions))
