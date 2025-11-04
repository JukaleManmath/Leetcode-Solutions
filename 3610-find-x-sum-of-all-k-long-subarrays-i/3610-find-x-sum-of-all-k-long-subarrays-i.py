class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        ans = []
        for i in range(n - k + 1):
            res = nums[i:i+k]
            count = Counter(res)
            if len(count) < x:
                ans.append(sum(res))
                continue
            heap = []
            for i in count:
                heapq.heappush(heap, (-count[i], -i))

            nr = []
            while len(nr) < x:
                cnt , num = heapq.heappop(heap)
                nr.append(num * cnt)
            
            ans.append(sum(nr))
        return ans
