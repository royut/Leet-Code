# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        numsDict = {}
        for i in range(len(nums)):
            numsDict[nums[i]] = 1
        curr = head
        while curr:
            # print(curr.val)
            # check next
            if curr.next and curr.next.val in numsDict:
                curr.next = curr.next.next
            else:
                curr = curr.next
        if head.val in numsDict:
            head = head.next
        return head


if __name__ == '__main__':
    print('in main')
    nums = [1, 2, 3]
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(Solution().modifiedList(nums, head))