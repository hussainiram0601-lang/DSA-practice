class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = s.strip().split()
        return len(word[-1])
        