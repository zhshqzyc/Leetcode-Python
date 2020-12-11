class Solution:
    from typing import List
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: return []
        
        dict = {
            0: "0",
            1: "1",
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }
        
        result = [""]
        for digit in digits:
            temp_list = []
            for char in dict[int(digit)]:
                for c in result: 
                    temp_list.append(c+char)
            result = temp_list    
        return result    
    print(letterCombinations(None, '345'))       
