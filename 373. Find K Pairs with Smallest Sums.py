from heapq import *    
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        if not nums1 or not nums2: return []
        result = []
        prev = set((0,0))
        heap = [[nums1[0]+nums2[0],0,0]]
        while len(result)<k and heap:
            cur = heappop(heap)
            result.append([nums1[cur[1]],nums2[cur[2]]])
            if cur[1] < len(nums1)-1 and (cur[1]+1,cur[2]) not in prev:
                heappush(heap,[nums1[cur[1]+1]+nums2[cur[2]],cur[1]+1,cur[2]])
                prev.add((cur[1]+1,cur[2])) # 进过heap的位置，都加入到set里面进行记录
            if cur[2] < len(nums2)-1 and (cur[1],cur[2]+1) not in prev:
                heappush(heap,[nums1[cur[1]]+nums2[cur[2]+1],cur[1],cur[2]+1])
                prev.add((cur[1],cur[2]+1))
            #print(len(heap))
        return result