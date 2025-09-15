class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        end , start = len(s) -1, 0
        while s[end] == " ":
            end -= 1
        
        while s[start] == " ":
            start += 1

        while  start <= end:
            curr = ""
            while start <= end and s[start] != " ":
                curr += s[start]
                start += 1
            if curr:
                if res == "":
                    res = curr
                else:
                    res = curr + " " + res
            
            while start <= end and s[start] == " ":
                start += 1
        return res
