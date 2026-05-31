class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ##sort the list
        ##create result list which we return
        ##if the first val is greater than 0, return empty list
        ##if the index after 0 and is equal to the value at 0, continue
        ##assign beg and end pointer
        ##while beg less then end, calc thrd(val+beg+end)
        ##if thrd bigger than 0, make end smaller
        ##else do opposite
        ##if it is in, append and increment and decrement
        ##do another while with dupe check of left and beg<end
        ##if it is, increment beg by 1
        ##return list

        n, res = sorted(nums), []
        for i,j in enumerate(n):
            if j>0:
                break
            if i>0 and j == n[i-1]:
                continue
            l,r = i+1,len(n)-1
            while l<r:
                thrd = j+n[l]+n[r]
                if thrd > 0:
                    r-=1
                elif thrd < 0:
                    l+=1
                else:
                    res.append([j,n[l],n[r]])
                    l+=1
                    r-=1
                    while l<r and n[l] == n[l-1]:
                        l+=1
        return res
