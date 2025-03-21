class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        else:
            if list1.val >= list2.val:
                head = list2
                nex2 = list2.next
                nex1 = list1
            else:
                head = list1
                nex1 = list1.next
                nex2 = list2
        one = head
        while nex1 is not None and nex2 is not None:
            if nex1.val < nex2.val:
                one.next = nex1
                nex1 = nex1.next
            else:
                one.next = nex2
                nex2 = nex2.next
            one = one.next
        if nex1 is None:
            one.next = nex2
        else:
            one.next = nex1
        return head
    