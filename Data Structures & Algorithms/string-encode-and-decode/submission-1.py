class Solution:

    def encode(self, strs: List[str]) -> str:
        #encode using length of string and any character
        #going to use = as our char
        s = ""
        for i in strs:
            s += str(len(i)) + "=" + i

        return s


    def decode(self, s: str) -> List[str]:
        #create lst to keep track of words
        #create i to index
        #loop through length of the string from param
        #j will be where the number is
        #inner while finds number which is length of 
        #upcoming string
        #append the string starting from 1 after j
        # new i is one after the previouse word
        lst,i = [],0
        while i<len(s):
            j=i
            while s[j] != "=":
                j+=1
            length = int(s[i:j])
            lst.append(s[j+1:j+1+length])
            i = j+1+length
        return lst

