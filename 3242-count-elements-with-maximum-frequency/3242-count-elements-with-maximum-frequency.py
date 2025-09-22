class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = Counter(nums)
        maxfreq = 0
        for num in count:
            maxfreq = max(maxfreq, count[num])
        
        total = 0
        for num in count:
            if count[num] == maxfreq:
                total += maxfreq
            
        return total

