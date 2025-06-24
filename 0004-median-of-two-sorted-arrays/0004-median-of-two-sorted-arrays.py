class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_array = []
        m , n = len(nums1), len(nums2)
        i , j = 0, 0
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                merged_array.append(nums1[i])
                i += 1
            else:
                merged_array.append(nums2[j])
                j += 1
        while i < m :
            merged_array.append(nums1[i])
            i+= 1
        while j < n:
            merged_array.append(nums2[j])
            j += 1
        
        if (m + n) % 2 == 0:
            median = merged_array[(m+n-1)//2] + merged_array[((m+n-1)//2) + 1]
            median = median / 2  
        else:
            median = merged_array[(m +n-1)//2 ]

        return median
