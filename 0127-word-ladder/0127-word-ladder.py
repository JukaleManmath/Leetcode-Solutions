class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        nei = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] +"*"+ word[j+1:]
                nei[pattern].append(word)
        
        visited = set([beginWord])
        q = deque([beginWord])
        res = 1

        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neiword in nei[pattern]:
                        if neiword not in visited:
                            visited.add(neiword)
                            q.append(neiword)
            res += 1
        return 0
