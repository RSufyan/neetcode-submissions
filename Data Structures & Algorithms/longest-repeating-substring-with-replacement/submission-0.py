class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ##hashmap for occurences of each character
        ##res for longest substring with k repalcements(length of substring
        ##minus max count in hasmap >k)
        ##l  and right pointer from for loop
        ##
        ##
        count = {}
        res = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0)

            while (r-l+1) - max(count.values()) > k:
                count[s[l]] -=1
                l+=1

            res = max(res,r-l+1)
        return res
            
