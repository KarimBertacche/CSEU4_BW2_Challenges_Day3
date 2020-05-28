# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        newList = ListNode()
        list_head = newList

        while l1 and l2:
            if l1.val <= l2.val:
                newList.next = ListNode(l1.val)
                l1 = l1.next
            else:
                newList.next = ListNode(l2.val)
                l2 = l2.next
            newList = newList.next
        while l1:
            newList.next = ListNode(l1.val)
            newList = newList.next
            l1 = l1.next
        while l2:
            newList.next = ListNode(l2.val)
            newList = newList.next
            l2 = l2.next

        return list_head.next

# Input: 1->2->4
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

# Input: 1->3->4
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

result = Solution().mergeTwoLists(l1, l2)

# Output: 1->1->2->3->4->4
while result:
    print(result.val)
    result = result.next