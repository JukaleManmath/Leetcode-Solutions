class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        def issubfolder(f1 , f2):
            f1 , f2 = f1[1:] , f2[1:]
            f1_arr = f1.split("/")
            f2_arr = f2.split("/")
            return f1_arr == f2_arr[:len(f1_arr)]

        res = [folder[0]]
        curr = folder[0]

        for i in range(1, len(folder)):
            if issubfolder(curr, folder[i]):
                continue
            res.append(folder[i])
            curr= folder[i]
        return res