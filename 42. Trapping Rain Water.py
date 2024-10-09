height = [0,1,0,2,1,0,1,3,2,1,2,1]
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)
        left_array = [0] * n
        right_array = [0] * n
        left_max = right_max = 0

        for i in range(n):
            j = -i-1

            left_array[i] = left_max
            right_array[j] = right_max

            left_max = max(left_max,height[i])
            right_max = max(right_max,height[j])

        water_stored = 0
        for i in range(n):
            potential = min(left_array[i] , right_array[i])
            water_stored = water_stored + max(0, potential - height[i])
        return water_stored


instance1 = Solution()
print(instance1.trap(height))