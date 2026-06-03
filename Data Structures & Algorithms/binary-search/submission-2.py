class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ##have l and r pointer
        ##while l<=r, define a mid point
        ##if target is > m, update the l
        ##elif, target < m, update r
        ##else return m
        ##if not in array, return -1

        l,r = 0, len(nums)-1
        while l<=r:
            m = (l+r)//2
            if nums[m]>target:
                r= m-1
            elif nums[m]<target:
                l= m+1
            else:
                return m
        return -1
