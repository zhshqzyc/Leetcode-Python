class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        else:
            s = str(x)
            l = 0
            r = len(s) - 1
            while(l < r):
                if s[l] != s[r]:
                    return False
                else:
                    l += 1
                    r -= 1
        return True

s = Solution()
print(s.isPalindrome(121))
print(s.isPalindrome(-121)) 
print(s.isPalindrome(12))   
