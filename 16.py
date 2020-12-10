class Solution:
    from typing import List
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        result = nums[0] + nums[1] + nums[-1]
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                val = nums[i] + nums[l] + nums[r]
                if val == target:
                    return target
                if abs(val - target) < abs(result - target):
                    result = val
                if val < target:
                    l += 1
                else:
                    r -= 1
        return result  
    print(threeSumClosest(None, [-1,2,1,-4], 1))
