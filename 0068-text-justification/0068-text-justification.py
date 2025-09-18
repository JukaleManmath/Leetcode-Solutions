class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line = []
        line_len = 0
        for word in words:
            if line_len + len(line) + len(word) <= maxWidth:
                line.append(word)
                line_len += len(word)
            else:
                res.append(line)
                line = [word]
                line_len = len(word)
        res.append(line)
        justified_lines= []

        for i in range(len(res) - 1):
            line = res[i]
            numspaces = maxWidth - sum(len(word) for word in line)
            numgaps = max(len(line) -1 , 1)
            spaces_per_gap = numspaces // numgaps
            extraspaces = numspaces % numgaps

            justified_line = ""

            for word in line:
                justified_line += word
                if numgaps > 0:
                    justified_line += " " * (spaces_per_gap + (1 if extraspaces >0 else 0))
                    numgaps -= 1
                    extraspaces -= 1
            justified_lines.append(justified_line)

        last_line = " ".join(res[-1])
        last_line += " "* (maxWidth - len(last_line))
        justified_lines.append(last_line)
        
        return justified_lines

