# True
s_1 = "racecar"
t_1 = "carrace"

# False
s_2 = "jar"
t_2 = "jam"

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26

        for char in s:
            idx = ord(char) - ord('a')
            count[idx] += 1

        for char in t:
            idx = ord(char) - ord('a')
            count[idx] -= 1
            if count[idx] < 0:
                return False

        return True


for s, t in [(s_1, t_1), (s_2, t_2)]:
    print(Solution().isAnagram(s, t))

"""
n = len(s) + len(t)
time - O(n)

memory - O(1)
"""