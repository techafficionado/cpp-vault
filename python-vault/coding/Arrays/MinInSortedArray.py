# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/solution/
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = nums
        start = 0
        end = len(arr) -1
        
        # 1 element array
        if start == end:
            return arr[start]
        # array is already sorted - no rotation
        if arr[end] > arr[start]:
            return arr[start]
        mid = start + (end-start)/2
        minidx = None
        while start < end:
            mid = start + (end-start)/2
            #print("start:{} end:{} mid:{}".format(start,end,mid))
            # implies element is on right side of mid
            if arr[mid] > arr[start]:
                # include mid element too just in case it is part of inflection point Eg: [4,5,6,7,0,1,2]
                start = mid
            elif arr[mid] < arr[start]:
                end = mid 
            elif arr[mid] == arr[start]:
                if arr[start] > arr[end]:
                    minidx = arr[end]
                    break
                else:
                    minidx = arr[start]				
                    break

        if minidx is not None:
            return minidx

