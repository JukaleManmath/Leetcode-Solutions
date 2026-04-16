class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        """{
            1 : [0, 2, 4],
            3: [1, 4],
            4: [3],
            2: [6]
        }"""

        mp = defaultdict(list)
        n = len(nums)
        for i in range(n):
            mp[nums[i]].append(i)
        
        res = []
        for q in queries:
            curr = mp[nums[q]]
            m = len(curr)
            if m <= 1:
                res.append(-1)
                continue
            
            l ,r = 0 , m - 1
            while l <= r:
                mid = ( l + r) // 2
                if curr[mid] == q:
                    if mid == 0:
                        res.append(min(curr[mid + 1] - curr[mid], n - (curr[-1] - curr[mid])))
                    elif mid == m - 1:
                        res.append(min(curr[mid] - curr[mid - 1], n - (curr[mid] - curr[0])))
                    else:
                        res.append(min(curr[mid + 1] - curr[mid], curr[mid] - curr[mid - 1]))        
                    break
                
                elif curr[mid] < q:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return res
                

