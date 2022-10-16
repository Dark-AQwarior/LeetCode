class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = str(x)
        if a[0]=='-':
            return False
        else:
            z = a[::-1]
            return int(z)==int(x)