class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def devoweled(s):
            return "".join("*" if c in "aeiou" else c for c in s)
        
        exact = set(wordlist)
        casemap = {}
        vowelmap = {}

        for w in wordlist:
            lower = w.lower()
            devowel = devoweled(lower)

            if lower not in casemap:
                casemap[lower] = w
            if devowel not in vowelmap:
                vowelmap[devowel] = w
        
        answer = []

        for q in queries:
            if q in exact:
                answer.append(q)
            else:
                qlower = q.lower()
                qdevowel = devoweled(qlower)
                if qlower in casemap:
                    answer.append(casemap[qlower])
                elif qdevowel in vowelmap:
                    answer.append(vowelmap[qdevowel])
                else:
                    answer.append("")
        
        return answer