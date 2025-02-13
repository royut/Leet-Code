# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        while (head):
            if head.val == None:
                return True
            else:
                head.val = None
                head = head.next
        return False


if __name__ == '__main__':
    print(1)