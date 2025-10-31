class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged_list = nums1 + nums2
        merged_list.sort()
        length = len(merged_list)
        mid = length // 2
        if length % 2 == 1:
            return float(merged_list[mid])
        else:
            return (merged_list[mid - 1] + merged_list[mid]) / 2.0