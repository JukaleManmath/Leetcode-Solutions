class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mp = defaultdict(int)
        n = len(numbers)

        for i in range(n):
            if numbers[i] in mp:
                return [mp[numbers[i]] , i + 1]
            mp[target - numbers[i]] = i + 1
        
            