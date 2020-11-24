class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = -1
        maxlength = 0
        dict = {}
        for i in range(len(s)):
            if s[i] in dict and dict[s[i]] > start:
                start = dict[s[i]]
                dict[s[i]] = i
            else:
                dict[s[i]] = i
                if (i - start) > maxlength:
                    maxlength = i- start
        return maxlength

s = Solution() 
print('abcabcbb maxlength =', s.lengthOfLongestSubstring('abcabcbb'))
print('bbbb maxlength =', s.lengthOfLongestSubstring('bbbb'))
print('pwwkew maxlength =', s.lengthOfLongestSubstring('pwwkew'))
