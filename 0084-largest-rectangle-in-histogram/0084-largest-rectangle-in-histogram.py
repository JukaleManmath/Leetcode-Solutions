class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ma = 0
        st = []

        for i, v in enumerate(heights):
            start =i
            while st and st[-1][1] > v:
                idx, height = st.pop()
                ma = max(ma , (i - idx) * height)
                start  = idx
            
            st.append((start, v))
        
        for i , h in st:
            ma = max(ma , (len(heights) - i) * h)
        return ma