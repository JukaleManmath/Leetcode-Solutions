class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort()
        mp = defaultdict(list)

        for i in arr:
            mp[bin(i).count("1")].append(i)
        
        res = []
        for i in range(14):
            if i in mp:
                for num in mp[i]:
                    res.append(num)
        
        return res