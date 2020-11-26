class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindrome = ''
        
        for i in range(len(s)):
            s1 = self.getlongestpalindrome(s, i, i)
            len1 = len(s1)
            if (len1 > len(palindrome)):
                palindrome = s1
                
            s2 = self.getlongestpalindrome(s, i, i + 1)  
            len2 = len(s2)
            if (len2 > len(palindrome)):
                palindrome = s2
                
        return palindrome  
    
    def getlongestpalindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1 
            r += 1
        return s[l + 1 : r]    

solution = Solution() 
print(solution.longestPalindrome('babad'))
