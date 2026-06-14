# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        # print(arr)
        n = len(arr)
        maxTwinSum = arr[0] + arr[-1]
        for i in range(1, n//2):
            if arr[i] + arr[n-i-1] > maxTwinSum:
                maxTwinSum = arr[i] + arr[n-i-1]
        return maxTwinSum


if __name__ == "__main__":
    print('in main')
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    print(Solution().pairSum(head))

