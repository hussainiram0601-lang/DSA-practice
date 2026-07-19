class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # Step 1: Record the last occurrence index of each character
        last_occurrence = {char: idx for idx, char in enumerate(s)}
        
        stack = []
        seen = set()
        
        # Step 2: Iterate through the string
        for idx, char in enumerate(s):
            # If character is already in the result stack, skip it
            if char in seen:
                continue
                
            # Pop characters from stack if they are lexicographically larger 
            # than the current char and occur again later in the string
            while stack and stack[-1] > char and last_occurrence[stack[-1]] > idx:
                removed_char = stack.pop()
                seen.remove(removed_char)
                
            # Add the current character to the stack and seen set
            stack.append(char)
            seen.add(char)
            
        return "".join(stack)
        