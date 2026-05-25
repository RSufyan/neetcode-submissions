class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]: 
        #create a new array
        #for mulitply every number that isnt the current i number
        #add the product to the current i place (list[i] = prod)
        #return the list
        lst  = [0]*len(nums)
        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                prod *= nums[j]
            lst[i] = prod
        return lst
        