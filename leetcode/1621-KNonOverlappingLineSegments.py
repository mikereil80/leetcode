class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        dp = [0] * (n - 1) + [1]
        for j in range(1, k + 1):
            dp2 = [0] * n
            acc, pre = 0, 0
            for i in range(n - 2, -1, -1):
                pre += dp[i + 1]
                acc += pre
                dp2[i] = acc if (n - i) >= j else 0
            dp = dp2
        return sum(dp) % (10 ** 9 + 7)