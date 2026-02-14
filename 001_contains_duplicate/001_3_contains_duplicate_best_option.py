from typing import List

nums_1 = [1, 2, 3, 3]
nums_2 = [1, 2, 3, 4]


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return not len(set(nums)) == len(nums)


for nums in [nums_1, nums_2]:
    print(Solution().hasDuplicate(nums))

"""
time - O(n)
memory - O(n)
"""