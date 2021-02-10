# Solution 1 : BFS, O(n) time complexity and O(n) space complexity
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # get the size of the grid
        n = len(grid)
        # if we have grid length 1 and the value is 1
        # then there is no clear path and return -1
        if grid[0][0] == 1:
            return -1
        # otherwise let's go for bfs from the strating cell (0,0)
        # a hashtable we need to maintain to update the neighbors distance from the current node.
        # note that beacuse of using a hashtable we don't need to maintain  a visited hash set
        # to track whether the neighbor is visited
        # the hashtable is has default values for it's key set as -1
        neighbor_dist = {}
        neighbor_dist = defaultdict(lambda:-1, neighbor_dist)
        # need deque for bfs
        dq = deque([(0,0)])
        neighbor_dist[(0,0)] = 0
        # until this deque is not empty
        while dq:
            # we popleft from the dq and get the node coordinates that we need to explore now
            r, c = dq.popleft()
            # we ccheck it's neighbors, in all 8 directions
            for nr,nc in [(r-1,c), (r+1,c), (r,c-1), (r, c+1), (r-1,c-1), (r+1, c-1), (r-1, c+1), (r+1,c+1)]:
                # if the neighbors are valid and if they don't contain 1 and if they are not 
                # visited already (check by hashtable value for this neighbor indice)
                # then we update that neighbor's distance from the current node that we are exploring
                if (0<=nr<n) and (0<=nc<n) and grid[nr][nc] != 1 and neighbor_dist[(nr,nc)] == -1 :
                    neighbor_dist[(nr,nc)] = neighbor_dist[(r,c)] + 1
                    # then we append the neighbor coordinate in the dq
                    dq.append((nr,nc))
        # print(neighbor_dist)
        # we return the distance for grid [n-1][n-1]. If it can be reached then the distnace
        # must be not the dafault value(-1). we add +1 because we put the distance as a edge.
        # so number of nodes are 1 more than that.
        return neighbor_dist[(n-1,n-1)] + 1 if neighbor_dist[(n-1,n-1)] > -1 else -1