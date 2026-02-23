from typing import List

examples = [
    ([3,4,5,6], 7), # [0,1]
    ([4,5,6], 10), # [0,2]
    ([5,5], 10), # [0,1]
    ([2,5,5,11], 10) # [1,2]
]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]



for nums, target in examples:
    print(Solution().twoSum(nums, target))

"""
time - O(n^2)
memory - O(1)
"""