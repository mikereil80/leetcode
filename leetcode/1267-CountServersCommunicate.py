class Solution:

    def countServers(self, grid: List[List[int]]) -> int:
        row = defaultdict(set)
        col = defaultdict(set)
        visited = set()
		##Add all indexes to map which have servers
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    row[i].add(j)
                    col[j].add(i)
         
        count = 0
		##count through rows which have more than one server ;keep a visited set to avoid double counting 
        for x,y in row.items():
            if len(y) > 1:
                for j in y:
                    if (x,j) not in visited:
                        visited.add((x,j))
                        count += 1
        
		##count through cols which have more than one server; keep a visited set to avoid double counting 
        for y,x in col.items():
            if len(x) > 1:
                for j in x:
                    if (j,y) not in visited:
                        #print(j,y)
                        visited.add((j,y))
                        count += 1
           
        return count