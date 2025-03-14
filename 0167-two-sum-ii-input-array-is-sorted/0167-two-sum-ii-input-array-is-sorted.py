class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        mp = defaultdict(int)
        for i in range(len(numbers)):
            temp = target - numbers[i]
            if mp[temp]:
                return [mp[temp] , i+1]
            mp[numbers[i]] = i + 1
        
        return []