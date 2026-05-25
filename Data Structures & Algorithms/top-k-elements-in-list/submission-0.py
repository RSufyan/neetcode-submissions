class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #convert to dict and keep track of # of each num
        dic = defaultdict(int)
        for n in nums:
            dic[n] +=1
        #order dict
        sorted_d = dict(sorted(dic.items(),key=lambda x:x[1],reverse=True))
        #check the first k keys
        keys = list(sorted_d.keys())
        new_list = []
        for i in keys[:k]:
            new_list.append(i)
        return new_list        