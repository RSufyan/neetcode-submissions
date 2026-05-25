class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = defaultdict()
        #make a new dic with key: num val: inex
        #check if comp in dic
        #if in, return val of comp and curr index
        #else add curr to dic
        for i,n in enumerate(nums):
            comp = target-n
            if comp in dic:
                return[dic[comp],i]
            dic[n]=i

        