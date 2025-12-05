class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        n = len(nums)
        ps = [0] * n
        ps[0] = nums[0]
        for i in range(1, n):
            ps[i] = ps[i-1] + nums[i]
        
        partitions = 0

        for  i in range(n-1):
            if ( 2 * ps[i] - ps[-1]) % 2 == 0:
                partitions += 1
        return partitions