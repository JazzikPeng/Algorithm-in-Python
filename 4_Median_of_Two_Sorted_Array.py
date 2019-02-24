# I wrote the merge two sorted array step recursively.
# This is rather slow but within the expected time complexity.
# Use python sorted() for the best performance.


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # merge sorted array
        def findMedian(arr):
            n = len(arr)
            if n % 2 == 0:
                return (arr[n//2-1] + arr[n//2]) / 2
            else:
                return arr[n//2]

        if len(nums1) < 1:
            return findMedian(nums2)
        if len(nums2) < 1:
            return findMedian(nums1)

        def mergeTwoLists(arr1, arr2, arr1_idx=0, arr2_idx=0):
            temp = []
            if arr1_idx >= len(arr1):
                t = arr2_idx
                return arr2[t:]
            if arr2_idx >= len(arr2):
                t = arr1_idx
                return arr1[t:]
            if arr1[arr1_idx] <= arr2[arr2_idx]:
                temp.append(arr1[arr1_idx])
                temp.extend(mergeTwoLists(arr1, arr2, arr1_idx+1, arr2_idx))
            else:
                temp.append(arr2[arr2_idx])
                temp.extend(mergeTwoLists(arr1, arr2, arr1_idx, arr2_idx+1))
            return temp
        temp = mergeTwoLists(nums1, nums2)
        n = len(nums1) + len(nums2)
        if n % 2 == 0:
            return (temp[n//2-1] + temp[n//2]) / 2
        else:
            return temp[n//2]
