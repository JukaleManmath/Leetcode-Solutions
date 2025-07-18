class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            idx = ord(c) - ord('a')
            if curr.children[idx] is None:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        curr.isEndOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            idx = ord(c) - ord('a')
            if curr.children[idx] is None:
                return False
            curr = curr.children[idx]
        return curr.isEndOfWord
        
    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            idx = ord(c) - ord('a')
            if curr.children[idx] is None:
                return False
            curr = curr.children[idx]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)