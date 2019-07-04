class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # t = sorted(nums1[:m]+nums2)
        # for i in range(len(t)):
        #     nums1[i] = t[i]
        j = 0
        for i in range(n):
            num = nums2[i]
            while nums1[j] <= num and j < m + i:
                j += 1
            nums1.insert(j, num)
            j += 1
            nums1.pop(-1)
