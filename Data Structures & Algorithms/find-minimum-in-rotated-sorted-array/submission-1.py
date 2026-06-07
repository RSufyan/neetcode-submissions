class Solution:
    def findMin(self, nums: List[int]) -> int:
        ##left and right pointer and find middle index
        ##if val at middle index<= left index val, search right side 
        ##else search left side, repeat process
        ## if it went right side and l val is < r val, return l val

        l,r = 0,len(nums)-1
        while l<r:
            m = ((l+r)//2)
            if nums[m] < nums[r]:
                r = m
            else:
                l = m+1
        return nums[l]
