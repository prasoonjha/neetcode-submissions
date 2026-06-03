class Solution:
    
    def findLocation(self, r: int, c: int) -> List[int]:
        return (r//3, c//3)
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # When will I know the sudoku is valid. I need to validatee each box.
        # if i know the number of emties in a row, if x rows are empty,
        # i can place numbers from 10-x possible digits. to find if a given 
        # sudoku is valid, do we need to solve the sudoku board. we could use a 
        #set to track all the digits in any row col r,c and the sub-cube it is in.
        #how to know which cube any r, c belongs to. there are 8 sub-cubes indexed 0
        """
            WARNING: this is not a dfs/ neither a backtracking problem. use 3 sets to confirm 3 constraints
            for each element.
            each (r,c) belongs to a sub cube. we could figure that outby taking a r%3
            and c//3 for example, (3,3) would lie in the 0th subcube.8, 8 should be 2,2
            so, we know which row, col and cube the given  r,c belongs to. next,
            all numbers in the set tracking these spaces should never see a repeat elment
            no, so a row can contain digits from 0 to 9 and the col could also be a separate
            set, 
            wait, we need to skip r,c "" s because we only need to verify the nums that 
            are there on the board, so each num (r, c) at is in 3 different sets which
            could have things in common but don't necessarily

        """
        ROWS = 9
        COLS = 9
        row_dict = defaultdict(set)
        col_dict = defaultdict(set)
        cube_dict = defaultdict(set)
        # def dfs(self, r, c, i):
        #     #returns nothing, updates isValid
        #     if r<0 or c<0 or r==ROWS or c==COLS or board[r][c] == "":
        #         return

            
        #     dfs(r, c+1, board[r][c+1])
        #     dfs(r, c-1, board[r][c-1])
        #     dfs(r+1, c, board[r+1][c])
        #     dfs(r-1, c, board[r-1][c])



        for r in range(ROWS):
            for c in range(COLS):
                num = board[r][c]
                if num == ".":
                    continue
                else:
                    x, y = self.findLocation(r,c)
                    if num in row_dict[r] or num in col_dict[c] or num in cube_dict[(x,y)]:
                        return False
                    row_dict[r].add(num)
                    col_dict[c].add(num)
                    cube_dict[(x, y)].add(num)
                    
        return True

        
                
            