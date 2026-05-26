class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = set(nums)
        #create max len list
        max_len_lst = []
        #loop thru nums and have key be first num
        for i in nums:
            key = i
            max_len = 1
        #then nest another loop
            for j in nums:
        #then search nested loop for key+1
                if key+1 in nums:
        #if exists, increment max len by 1
                    max_len +=1
        #get key equal to number and repeat
                    key +=1
        #append js max len to list
            max_len_lst.append(max_len)
        #return max max len
        return max(max_len_lst)
