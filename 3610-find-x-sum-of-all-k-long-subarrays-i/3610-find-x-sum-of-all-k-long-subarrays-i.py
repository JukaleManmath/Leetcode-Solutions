class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        ans = []
        for i in range(n - k + 1):
            res = nums[i:i+k]
            count = Counter(res)
            heap = []
            for i in count:
                heapq.heappush(heap, (-count[i], -i))

            nr = []
            while len(nr) < x and heap:
                cnt , num = heapq.heappop(heap)
                nr.append(num * cnt)
            
            ans.append(sum(nr))
        return ans
