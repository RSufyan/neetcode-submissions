class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ##create beg and end index
        ##check 2 vals at i and j are not equal
        ##if not, check if the 2 equal target
        n = numbers
        i, j = 0, len(n)-1
        print(j)
        while i<j:
            if n[i] != n[j]:
                if n[i] + n[j] == target:
                    return [i+1,j+1]
                if n[i] + n[j] > target:
                    j-=1
                    continue
                if n[i] + n[j] < target:
                    i+=1
                    continue
            j-=1
        