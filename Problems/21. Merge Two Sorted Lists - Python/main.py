# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def iter(self):
        here = self
        while here:
            print(here.val, end=" ")
            here = here.next
        print(" ")


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        mergedList = ListNode()
        first = mergedList
        before = None
        while list1 or list2:
            if list1 and list2:
                if list1.val < list2.val:
                    mergedList.val = list1.val
                    mergedList.next = ListNode()
                    list1 = list1.next
                else:
                    mergedList.val = list2.val
                    mergedList.next = ListNode()
                    list2 = list2.next
            elif list1:
                mergedList.val = list1.val
                mergedList.next = ListNode()
                list1 = list1.next
            else:
                mergedList.val = list2.val
                mergedList.next = ListNode()
                list2 = list2.next
            before = mergedList
            mergedList = mergedList.next

        try:
            before.next = None
        except:
            return None
        return first


if __name__ == '__main__':
    print('in main')
    head1 = ListNode(1, ListNode(2, ListNode(1, ListNode(2, ListNode(1, ListNode(2))))))
    head2 = ListNode(3, ListNode(4, ListNode(3, ListNode(4, ListNode(3, ListNode(4))))))
    new = (Solution().mergeTwoLists(None, None))
    new.iter()
