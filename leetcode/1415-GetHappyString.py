class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        letters = ['a', 'b', 'c']
        def dfs(curr):
            if len(curr) == n:
                yield curr
            else:
                for i in range(len(letters)):
                    if not curr or curr and curr[-1] != letters[i]:
                        yield from dfs(curr + letters[i])
        for i, ans in enumerate(dfs('')):   
            if i == k - 1: 
                return ans
        return ''