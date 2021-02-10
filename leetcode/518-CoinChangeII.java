class Solution {
    public int change(int amount, int[] coins) {
        int[][] dp = new int[coins.length][amount + 1];
        for(int i = 0; i < coins.length; i++){
            Arrays.fill(dp[i], -1);
        }
        return cc(coins, 0, amount, dp);
    }
    
    int cc(int[] coins, int i, int amount, int[][] dp){
        if(amount == 0) return 1;
        if(amount < 0 || i == coins.length) return 0;
        if(dp[i][amount] != -1) return dp[i][amount];
        
        return dp[i][amount] = cc(coins, i, amount - coins[i], dp) + cc(coins, i + 1, amount, dp);
    }
    
}