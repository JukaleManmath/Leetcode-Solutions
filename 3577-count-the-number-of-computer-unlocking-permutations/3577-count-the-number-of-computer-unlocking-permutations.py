class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        n = len(complexity)
        smallest = complexity[0]
        mod = 10 ** 9 + 7

        mp = defaultdict(int)
        for i in range(1, n):
            if complexity[i] <= smallest:
                return 0
            mp[complexity[i]] += 1
        
        div = 1
        for i in mp:
            div *= mp[i]
        ans = 1
        for i in range(1, n):
            ans *= i
        return (ans) % mod
