class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total = sum(apple)
        capacity.sort()
        n = len(capacity)
        for i in range( n -1 , -1, -1):
            if total <= capacity[i]:
                return n - i
            else:
                total -= capacity[i]
        