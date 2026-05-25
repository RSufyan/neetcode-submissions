class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #convert to dict and keep track of # of each num
        dic = defaultdict(int)
        for n in nums:
            dic[n] +=1
        #order dict
        heap = [        ]        
        for ke,v in dic.items():
            heapq.heappush(heap,(v,ke))
            if len(heap)>k:
                heapq.heappop(heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res




