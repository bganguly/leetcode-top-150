import collections
from collections import deque

class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        # Decide on the size of the board
        size = len(board)
        maxsquare = size*size

        def numtorowcol(n):
            row = (maxsquare-n)/size
            # This in the range of 0 to 2 * size - 1
            c = (n-1) % (2*size)        
            if c < size:
                col = c
            else:
                col = 2*size-1-c
            return (row,col)
        
        def minmoves(n):
            q = collections.deque([n])
            visited = {}
            # records shortest path distance from source to this vertex
            visited[n] = 0 
            while len(q) != 0:
                curr = q.popleft()
                for i in range(1,7):
                    nxt = curr + i
                    if nxt > maxsquare:
                        continue
                    (r,c) = numtorowcol(nxt)
                    print()
                    print(r,c)
                    print()
                    if board[r][c] != -1:
                        nxt = board[r][c]
                    if nxt not in visited:
                        q.append(next)
                        visited[nxt] = visited[curr] + 1
                        if nxt == maxsquare:
                            return visited[nxt]
            return -1
        
        return minmoves(1)

board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]    
print(Solution().snakesAndLadders(board))
