class Solution:
    def hIndex(self, citations: List[int]) -> int:

        #  Brute force - O(n2)
        # max_h = 0
        # n = len(citations)
        # for i in range(1, n+1):
        #     cnt = 0
        #     for j in range(n):
        #         if citations[j] >= i:
        #             cnt += 1
        #         if cnt == i:
        #             max_h = max(max_h, cnt)
        #             break
        # return max_h

        # so the optimized wayy is to like sort or store the count of papers , index as the number of citations and 
        # we know the citations are between 0 - n
        # and we come from max h(last index) in reverse order checing if the h has atleast h paper
        # we use commulatative for it

        paper = len(citations)
        cnt = [0] * (paper + 1)

        for citation in citations:
            cnt[min(citation, paper)] += 1
        
        comm = 0
        for i in range(paper, -1, -1):
            comm += cnt[i]
            if comm >= i:
                return i
                