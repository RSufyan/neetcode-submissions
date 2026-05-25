class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #itt thru aray
        #if visited, check
        #if not, add to vis list

        vis_set =  set()
        for x in nums:
            if x in vis_set:
                return True
            else:
                vis_set.add(x)
        return False



        
