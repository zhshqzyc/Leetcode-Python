class Solution:
    from typing import List
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs or strs == ['']:
            return ''
        first_string = strs[0]
        for i in range(len(first_string)):
            for s in strs[1:]:
                if i >= len(s) or s[i] != first_string[i]:
                    return first_string[:i]
        return strs[0]        
    strs = ["flower","flow","flight"]
    print(longestCommonPrefix(None, strs))
