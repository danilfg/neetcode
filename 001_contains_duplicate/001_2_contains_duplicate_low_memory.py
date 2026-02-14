from typing import List

nums_1 = [1, 2, 3, 3] # True
nums_2 = [1, 2, 3, 4] # False


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False


for nums in [nums_1, nums_2]:
    print(Solution().hasDuplicate(nums))

"""
memory - O(1) or O(log n) or O(n log n) or O(n)
time - O(n log n)
"""