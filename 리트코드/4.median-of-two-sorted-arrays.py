class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_list = nums1 + nums2
        new_list.sort()
        if len(new_list) == 1:
            return new_list[0]
        elif len(new_list) % 2 == 1:
            return new_list[len(new_list) // 2]
        else:
            return (new_list[len(new_list) // 2] + new_list[len(new_list) // 2 - 1]) / 2

