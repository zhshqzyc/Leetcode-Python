class Solution:
   def reverse(self, x: int) -> int:
        result = int(str(abs(x))[::-1])
        if x > 0:
            return result if result < 2**31 - 1 else 0
        else:
            return -result if result < 2**31 else 0
            
s = Solution()
print(s.reverse(1534236469))  
