class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s = []
        while head is not None:
            s.append(head.val)
            head = head.next
        return s == s[::-1]
    