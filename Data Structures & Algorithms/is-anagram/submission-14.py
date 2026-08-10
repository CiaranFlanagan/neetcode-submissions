class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_letter_count = defaultdict(int)
        t_letter_count = defaultdict(int)
        for char in s:
            s_letter_count[char] += 1
        for char in t:
            t_letter_count[char] += 1
        return s_letter_count == t_letter_count





        