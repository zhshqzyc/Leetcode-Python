class Solution:
    def intToRoman(self, num: int) -> str:
        keys =   [1000, 900, 500, 400,
                  100,  90,  50,  40,
                  10,   9,   5,   4,
                  1]
        values = ['M', 'CM', 'D', 'CD',
                  'C', 'XC', 'L', 'XL',
                  'X', 'IX', 'V', 'IV',
                  'I']
        result = ''
        for i in range(len(keys)):
            while num >= keys[i]:
                num -= keys[i]
                result += values[i]
        return result
