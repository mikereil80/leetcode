class WordDictionary {

    /** Initialize your data structure here. */
    private class TrieNode{
        TrieNode[] links;
        boolean isWord;
        
        TrieNode(){
            links = new TrieNode[26];
            isWord = false;
        }
    }
    
    TrieNode root; 
    public WordDictionary() {
        root = new TrieNode();
    }
    
    public void addWord(String word) {
         TrieNode p = root;
         for(char c : word.toCharArray()){
             int index = c - 'a';
             if(p.links[index] == null){
                  p.links[index] = new TrieNode();            
             }
             p = p.links[index];
         }
         p.isWord = true;
         return;
    }
    
    public boolean search(String word) {
        return dfs(root, word);
    }
    
    public boolean dfs(TrieNode root, String word){
        TrieNode p = root;
        for(int i = 0; i < word.length(); i++){
             char c = word.charAt(i);
             if(c == '.'){
                 for(int k = 0; k < 26; k++){
                     if(p.links[k] != null){
                         if(dfs(p.links[k], word.substring(i + 1))){
                             return true;
                         }
                     }
                 }
                 return false;
             }
            // else 
             int index = c - 'a';
             if(p.links[index] == null){
                  return false;            
             }
             p = p.links[index];
        }
        return p.isWord;
    }
}