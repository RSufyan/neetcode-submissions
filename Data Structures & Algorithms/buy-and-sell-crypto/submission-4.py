class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ##have a minimum price which we will set to 0
        ##have profit set to 0 to start
        ##loop through prices
        ##if price is less than min price, we update min price to new low
        ##then if price minus min p> profit, we update the new best profit
        
        minp = prices[0]
        maxprof= 0
        for p in prices:
            if p<minp:
                minp=p
            if p-minp>maxprof:
                maxprof= p-minp
        return maxprof

        