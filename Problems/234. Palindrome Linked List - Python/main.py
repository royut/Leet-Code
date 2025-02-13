# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def iter(self):
        here = self
        while here:
            print(here.val)
            here = here.next


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        a = []
        while head:
            a.append(head.val)
            head = head.next

        for i in range(len(a)):
            if a[i] != a[len(a) - i - 1]:
                return False
        return True


if __name__ == "__main__":
    print("in main")
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(2, ListNode(1))))))
    print(Solution().isPalindrome(head))
