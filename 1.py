class Solution:
    from typing import List
    def twoSum(self, nums, target):
        dic={}
        for i in range(0 ,len(nums)):       
            if target-nums[i] in dic:return [dic[target-nums[i]],i]
            dic[nums[i]]=i
        
    print(twoSum(None, [3,2,4], 6))   
