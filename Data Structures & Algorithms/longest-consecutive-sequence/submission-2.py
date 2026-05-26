class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #var to track the max len
        res = 0
        #convert to set to have faster look ups
        store = set(nums)
        #loop thru nums
        for num in nums:
            #initialize the current streak and the current number
            streak, curr = 0, num
            #if in nums/store, increase streak and increase curr(looking for next num)
            while curr in store:
                streak += 1
                curr += 1
            #if not, get the max of that loop
            res = max(res, streak)
        #it will return max
        return res