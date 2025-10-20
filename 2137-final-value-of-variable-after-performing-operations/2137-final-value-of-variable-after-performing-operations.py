class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        total = 0
        for i in operations:
            if "--" in i:
                total -= 1
            else:
                total += 1
        return total