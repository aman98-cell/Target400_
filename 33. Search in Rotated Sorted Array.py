from typing import List
nums = [4,5,6,7,0,1,2]
target = 0

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in nums:
            if i == target:
                return nums.index(i)
        return -1
instance1 = Solution()
print(instance1.search(nums,target))

