class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last= {}
        for i , ch in enumerate(s):
            last[ch] = i
        res = []
        max_size = 0
        size = 0
        for i , char in enumerate(s):
            size += 1
            max_size = max(max_size, last[char])
            if i == max_size:
                res.append(size)
                size = 0
        return res

        
