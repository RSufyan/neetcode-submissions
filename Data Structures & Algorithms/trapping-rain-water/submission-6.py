class Solution:
    def trap(self, height: List[int]) -> int:
        ##left and right pointer
        ##vars for left and right tallest wall
        ##if left tallest, increment l by 1
        ##else decrement r by 1
        ## take max between the side you're looking at and reassign the tallest wall
        ## amount of rain is min(of tallest wall values)-value of current height

        l,r,maxl,maxr = 0,len(height)-1, height[0],height[len(height)-1]
        res = 0
        while l<r:
            if maxl<maxr:
                l+=1
                maxl = max(height[l],maxl)
                res += maxl -height[l]
            else:
                r-=1
                maxr = max(maxr,height[r])
                res += maxr-height[r]
        return res

            
            