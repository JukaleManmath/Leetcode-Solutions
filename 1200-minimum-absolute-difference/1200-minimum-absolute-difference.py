class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        res = []
        mindiff = float("inf")
        for i in range(len(arr) -1):
            if arr[i+1] - arr[i] < mindiff:
                res = [[arr[i], arr[i+1]]]
                mindiff = arr[i + 1] - arr[i]
            elif arr[i+1] - arr[i] == mindiff:
                res.append([arr[i], arr[i+1]])
            print(res)
            
        return res