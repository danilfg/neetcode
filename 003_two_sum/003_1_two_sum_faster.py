from typing import List

examples = [
    ([3,4,5,6], 7), # [0,1]
    ([4,5,6], 10), # [0,2]
    ([5,5], 10), # [0,1]
    ([2,5,5,11], 10) # [1,2]
]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            need = target - num

            if need in seen:
                j = seen[need]
                return [j, i] if j < i else [i, j]

            seen[num] = i

        return []


for nums, target in examples:
    print(Solution().twoSum(nums, target))

"""
time - O(n)
memory - O(n)
"""