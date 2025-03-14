class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        #using sorting  with O(m * nlogn). ans space compl. O(m * n)
        # res = defaultdict(list)

        # for s in strs:
        #     sorteds = "".join(sorted(s))
        #     res[sorteds].append(s)
        
        # return list(res.values())

        
        res = defaultdict(list)
        for s in strs:
            count= [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)
        return list(res.values())