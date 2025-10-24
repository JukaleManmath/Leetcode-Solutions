class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        n+=1

        def check(n):
            num = str(n)
            count = Counter(num)
            for i in count:
                if count[i] != int(i):
                    return False
            return True

        while True:
            if check(n):
                return n
            n += 1
        