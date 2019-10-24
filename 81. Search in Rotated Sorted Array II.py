class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        # O(n)
        # for i in nums:
        #     if i == target:
        #         return True
        # return False


        # convert rotated array back and use binary search  total: O(n)
        if not nums: return False
        pos = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                pos = i+1
                break
        nums = nums[pos:] + nums[:pos]

        def binary_search(arr, l, r, target):
            if l>r:
                return False
            mid = (l+r) // 2
            if target == arr[mid]:
                return True
            elif target < arr[mid]:
                return binary_search(arr, l, mid-1, target)
            else:
                return binary_search(arr,mid+1, r, target)

        return binary_search(nums, 0, len(nums)-1, target)