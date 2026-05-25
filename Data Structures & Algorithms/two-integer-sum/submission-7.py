class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = defaultdict()
        #make a new dic with key: num val: inex
        for i,n in enumerate(nums):
            comp = target-n
            if comp in dic:
                return[dic[comp],i]
            dic[n]=i

        