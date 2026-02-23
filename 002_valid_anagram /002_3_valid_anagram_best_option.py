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

        freq = {}

        for char in s:
            freq[char] = freq.get(char, 0) + 1

        for char in t:
            if char not in freq:
                return False
            freq[char] -= 1
            if freq[char] == 0:
                del freq[char]

        return len(freq) == 0

for s, t in [(s_1, t_1), (s_2, t_2)]:
    print(Solution().isAnagram(s, t))

"""
time - O(n)
memory - O(1) -> O(n)
"""