from typing import List
nums = [3,2,1,5,6,4]
k = 2

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]

instance1 = Solution()
print(instance1.findKthLargest(nums,k))
