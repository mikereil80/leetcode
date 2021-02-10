class Node:
    def __init__(self, val = 0, nxt = None):
        self.val = val
        self.nxt = nxt

class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        # convert to array
        head = Node()
        p = head
        for row in grid:
            for i in range(len(row)-1,-1,-1):
                if row[i] == 1: break
            p.nxt = Node(len(row)-1-i)
            p = p.nxt
        
        # find target one by one
        res = 0
        targets = list(range(len(grid)-1,-1,-1))
        for t in targets:
            q, p = head, head.nxt
            while p and p.val < t:
                p = p.nxt
                q = q.nxt
                res += 1
            if not p:
                return -1
            q.nxt = p.nxt
            
        return res