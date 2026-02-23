from typing import List

examples = [
    ([3,4,5,6], 7), # [0,1]
    ([4,5,6], 10), # [0,2]
    ([5,5], 10), # [0,1]
    ([2,5,5,11], 10) # [1,2]
]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = [(num, i) for i, num in enumerate(nums)]
        arr.sort(key=lambda p: p[0])

        l = 0
        r = len(arr) - 1

        while l < r:
            s = arr[l][0] + arr[r][0]

            if s == target:
                i = arr[l][1]
                j = arr[r][1]
                return [i, j]

            if s < target:
                l += 1
            else:
                r -= 1

        return []


for nums, target in examples:
    print(Solution().twoSum(nums, target))

"""
time - O(n log n)
memory - O(n)
"""