class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        arr1 = version1.split(".")
        arr2 = version2.split(".")
        
        m , n = len(arr1), len(arr2)
        for i in range(max(m , n)):
            v1 = int(arr1[i]) if i < m else 0
            v2 = int(arr2[i]) if i < n else 0

            if v1 > v2:
                return 1
            if v2 > v1:
                return -1

        return 0

            

        return 0              