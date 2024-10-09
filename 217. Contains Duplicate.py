from typing import List
nums = [1,2,3,5]


class Solution:

    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        emptySet = set()

        for i in range(n):
            if nums[i] in emptySet:
                return True
            else:
                emptySet.add(nums[i])
        return False

instance1 = Solution()
print(instance1.containsDuplicate(nums))