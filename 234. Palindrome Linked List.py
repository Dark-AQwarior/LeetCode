class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l = []
        while head!=None:
            l.append(head.val)
            head = head.next
        
        if l == l[::-1]:
            return True
        else:
            return False