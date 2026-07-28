class Solution:
    def smallestPalindrome(self, s: str) -> str:
        half = sorted(s[:len(s) // 2])
        mid = s[len(s) // 2] if len(s) % 2 == 1 else ""
        
        return "".join(half) + mid + "".join(half[::-1])
        