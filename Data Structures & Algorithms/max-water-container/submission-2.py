class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ##pointer to l and r and have the res set to 0. while l less r
        ##have max area, take min of length times distance between the 2
        ## res is set to the max of res and area
        ##if l val is greater or equal, increment by 1
        ##else, decrement by 1
        ##return res
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            res = max(res, area)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res