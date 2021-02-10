class Solution {
    public int balancedStringSplit(String s) {
        int balanced = 0, output = 0;
        for(char c: s.toCharArray()) {
            if (c == 'R') balanced++;
            else if (c == 'L') balanced--;
            if (balanced == 0) output++;
        }
        return output;
    }
}