class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #create dics for row, column, and squares
        #loop thru the max len of rows and columns which is 9
        #check if period if it is continue
        #check if the number ur at is in any of the dics
        #if it is then return false, if not add to dic
        #we use sets for quicker look ups
        
        
        
        r = defaultdict(set)
        c = defaultdict(set)
        s = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if (board[i][j] in r[i] 
                or board[i][j] in c[j] 
                or board[i][j] in s[i//3,j//3]):
                    return False
                r[i].add(board[i][j])
                c[j].add(board[i][j])
                s[i//3,j//3].add(board[i][j])

        return True




        