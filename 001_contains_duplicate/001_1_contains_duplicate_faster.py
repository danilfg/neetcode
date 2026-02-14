from typing import List

nums_1 = [1, 2, 3, 3]
nums_2 = [1, 2, 3, 4]


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

for nums in [nums_1, nums_2]:
    print(Solution().hasDuplicate(nums))

"""
memory - O(n)
time - O(n)
"""