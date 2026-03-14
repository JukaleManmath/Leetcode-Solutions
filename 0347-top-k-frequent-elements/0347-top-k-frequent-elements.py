class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = defaultdict(int)
        for i in nums:
            mp[i] += 1
        
        n = len(nums)
        freq = [[] for _ in range(n + 1)]

        for i in mp:
            freq[mp[i]].append(i)
        
        res = []
        for i in range(n, -1, -1):
            if len(freq[i]) > 0:
                for j in freq[i]:
                    res.append(j)
                    if len(res) == k:
                        return res
        

