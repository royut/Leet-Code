# Definition for a binary tree node.
import time


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree(object):
    def __init__(self, val=0, left=None, right=None):
        self.root = TreeNode(val, left, right)

    def insert_up(self, curr, parent, child, left):
        if curr is None:
            return
        if curr.val == parent:
            newNode = TreeNode(child)
            if left == 1:
                curr.left = newNode
                return
            else:
                curr.right = newNode
                return
        elif curr.val == child:
            newNode = TreeNode(parent)
            if left == 1:
                newNode.left = curr
            else:
                newNode.right = curr
            self.root = newNode
            return
        else:
            self.insert_up(curr.right, parent, child, left)
            self.insert_up(curr.left, parent, child, left)
            return

    def insert(self, parent, child, left):
        self.insert_up(self.root, parent, child, left)
        return

    def print_tree(self):
        nodes = [self.root]
        while nodes:
            curr = nodes.pop(0)
            print(curr.val, end=" ")
            if curr.left:
                nodes.append(curr.left)
            if curr.right:
                nodes.append(curr.right)


class Solution(object):
    def createBinaryTree(self, descriptions):
        """
        :type descriptions: List[List[int]]
        :rtype: Optional[TreeNode]
        """
        parents = set()
        children = set()
        for desc in descriptions:
            parents.add(desc[0])
            children.add(desc[1])
        rootVal = (parents - children).pop()
        tree = BinaryTree(rootVal)
        # print(rootVal)
        orderedDesc = []
        index = 0
        parents = set()
        parents.add(rootVal)
        added = set()
        while len(parents) != len(descriptions)+1:
            if descriptions[index][0] in parents and index not in added:
                orderedDesc.append(descriptions[index])
                parents.add(descriptions[index][1])
                added.add(index)
            index += 1
            if index == len(descriptions):
                index = 0
        #     print(parents, index)
        # print('o', orderedDesc)

        for desc in orderedDesc:
            tree.insert(desc[0], desc[1], desc[2])
            # print(tree.root.val)
        tree.print_tree()
        return tree.root


if __name__ == "__main__":
    print('in main')
    # descriptions = [[20, 15, 1], [20, 17, 0], [50, 20, 1], [50, 80, 0], [80, 19, 1]]
    # descriptions = [[1, 2, 1], [2, 3, 0], [3, 4, 1]]
    # descriptions = [[85, 82, 1], [74, 85, 1], [39, 70, 0], [82, 38, 1], [74, 39, 0], [39, 13, 1]]
    descriptions = [[39, 70, 1], [13, 39, 1], [85, 74, 1], [74, 13, 1], [38, 82, 1], [82, 85, 1]]
    tree = (Solution().createBinaryTree(descriptions))
