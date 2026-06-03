# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def append(self, l: Optional[ListNode], n: Optional[ListNode]):
        curr = l
        while curr.next:
            curr = curr.next
        curr.next = n
        return l
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        t, b = list1, list2
        dummy = ListNode()

        while t and b:
            
            val1 = t.val
            val2 = b.val
            if val1 == val2:
                #both values equal, append both and increment pointer
                self.append(dummy, ListNode(val1, None))
                self.append(dummy, ListNode(val2, None))
                t = t.next
                b = b.next
            if val1 < val2:
                #append val1, increment t, keep b same
                self.append(dummy, ListNode(val1))
                t = t.next
            if val1 > val2:
                #append val2, increment append both
                self.append(dummy, ListNode(val2))
                b = b.next
        if b:
            self.append(dummy, b)
        if t:
            self.append(dummy, t)

        return dummy.next
