class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ##pointer to l and r. while l less r
        ##have max area, take min of length times distance between the 2
        ##return max area
        ##
        ##
        l,r,max_a = 0, len(heights)-1,0
        for i in range(len(heights)):
            for j in range(len(heights)):
                curr = (j-i)*min(heights[i],heights[j])
                max_a = max(curr,max_a)
        return max_a