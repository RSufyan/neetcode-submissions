class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ##right side of window, max, and curr
        ##for y(right side of our window) in s, while sy in curr, 
        ##remove sx and slide l up by 1
        ##then add the char to curr and get new max

        x,maxl,curr = 0,0,set()
        for y in range(len(s)):
            while s[y] in curr:
                curr.remove(s[x])
                x+=1
            curr.add(s[y])
            maxl = max(maxl,y-x+1)
        return maxl

        