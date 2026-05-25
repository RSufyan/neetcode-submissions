class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]: 
        lst  = [0]*len(nums)
        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                prod *= nums[j]
            lst[i] = prod
        return lst
        