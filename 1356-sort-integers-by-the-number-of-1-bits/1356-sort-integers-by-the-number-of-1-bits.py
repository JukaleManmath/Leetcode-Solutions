class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # arr.sort()
        # mp = defaultdict(list)

        # for i in arr:
        #     cnt = sum( i >> bit & 1 for bit in range(32) )
        #     mp[cnt].append(i)
        
        # res = []
        # for i in range(14):
        #     if i in mp:
        #         for num in mp[i]:
        #             res.append(num)
        
        # return res

        return sorted(arr, key = lambda a: [bin(a).count("1"), a])
