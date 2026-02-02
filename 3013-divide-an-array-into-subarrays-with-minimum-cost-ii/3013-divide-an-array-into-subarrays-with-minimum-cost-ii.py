class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        # n = len(nums)
        # if not nums:
        #     return 0
        # l = 1
        # r = l + dist
        # cost = float("inf")
        # while r < n:
        #     heap = []
        #     for i in range(l ,r + 1):
        #         heapq.heappush(heap, nums[i])
            
        #     topk = k -1
        #     curri = 0
        #     while topk > 0:
        #         curri += heapq.heappop(heap)
        #         topk -= 1
        #     if curri < cost:
        #         cost = curri
            
        #     l += 1
        #     r += 1
        # return nums[0] + cost

        # optimized approach
        n = len(nums)
        small, large = SortedList(), SortedList()

        for i in range(1, dist +2):
            small.add((nums[i], i))
        
        while len(small) >= k:
            large.add(small.pop(-1))
        
        curr = sum(v for v , _ in small)
        res = curr

        for i in range(dist + 2, n):
            pkey = (nums[i -dist-1], i-dist -1)
            nkey = (nums[i], i)

            # remove left
            if pkey in small:
                small.discard(pkey)
                curr -= nums[i - dist - 1]
                if large:
                    l = large.pop(0)
                    small.add(l)
                    curr += l[0]
            elif pkey in large:
                large.discard(pkey)

            
            #add right
            small.add(nkey)
            curr += nums[i]
            if len(small) >= k:
                s = small.pop(-1)
                large.add(s)
                curr -= s[0]
            
            res = min(res, curr)
        
        return nums[0] + res