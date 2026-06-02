class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ##have l n r pointer
        ##have maxp start at 0
        ##diff of l to r is curr max
        ##take max between curr and maxp
        ##increment the bigger of l or r
        ##
        
        
        minp = prices[0]
        maxprof= 0
        for p in prices:
            if p<minp:
                minp=p
            if p-minp>maxprof:
                maxprof= p-minp
        return maxprof

        