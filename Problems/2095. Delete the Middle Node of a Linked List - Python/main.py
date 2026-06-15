# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr = head
        n = 0
        while curr:
            n += 1
            curr = curr.next
        # print(n, curr, n//2)
        if n == 1:
            return None
        curr = head
        i = 0
        while curr:
            if n//2 == i+1:
                # print(i, curr, curr.val)
                curr.next = curr.next.next
            curr = curr.next
            i += 1
        # curr = head
        # while curr:
        #     print(curr.val)
        #     curr = curr.next
        return head


if __name__ == "__main__":
    print('in main')
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    print(Solution().deleteMiddle(head))

