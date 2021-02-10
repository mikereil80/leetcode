import java.util.HashMap;

class Solution {
    public boolean isIsomorphic(String s, String t) {
        int lengthOfS = s.length();
        int lengthOfT = t.length();
        if (lengthOfS != lengthOfT)
            return false;
        else if(lengthOfS == 0)
            return true;
        HashMap<Character, Character> previousMatchingChar = new HashMap<Character, Character>();
        for (int i = 0; i < lengthOfS; i++){
            char sChar = s.charAt(i);
            char tChar = t.charAt(i);
            if (previousMatchingChar.containsKey(sChar) && previousMatchingChar.get(sChar) != tChar)
                return false;
            previousMatchingChar.put(sChar, tChar);
        }
        previousMatchingChar.clear();
        for (int i = 0; i < lengthOfT; i++){
            char sChar = s.charAt(i);
            char tChar = t.charAt(i);
            if (previousMatchingChar.containsKey(tChar) && previousMatchingChar.get(tChar) != sChar)
                return false;
            previousMatchingChar.put(tChar, sChar);
        }
        return true;
    }
}