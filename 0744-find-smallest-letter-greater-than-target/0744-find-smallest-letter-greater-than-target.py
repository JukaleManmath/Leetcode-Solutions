class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        for i in range(n):
            if ord(target) - ord("a") < ord(letters[i]) -ord("a"):
                return letters[i]
        return letters[0]