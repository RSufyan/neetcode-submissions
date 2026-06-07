class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ##if len s < len t, return ""
        ##have 2 hashmaps to track count of t and current sub strings amount of chars in t
        ##
        ##
        ##

        if t == "":
            return ""
        
        countT,window = {},{}

        for c in t:
            countT[c] = countT.get(c,0)+1
        
        have, need = 0, len(countT)
        res, resLen,l = [0,0], float("infinity"),0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c,0)
            if c in countT and window[c] == countT[c]:
                have +=1
            while have == need:
                if(r-l+1 <resLen):
                    resLen = r-l+1
                    res = [l,r]
                window[s[l]] -=1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -=1
                l+=1

        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""

        





