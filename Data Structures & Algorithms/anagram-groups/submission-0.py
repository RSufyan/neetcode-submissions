class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create a default dict of tuples
        dic = defaultdict(list)
        #itt thru list
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)-ord('a')] +=1
            dic[tuple(count)].append(s)
        return list(dic.values())
        #create count for each word
        #for each str, have asci key to rep the word as count
        #make that count as the key and add the regualr word to it
        #return the list of the values in the dicts
