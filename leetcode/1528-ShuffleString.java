class Solution {
    public String restoreString(String s, int[] indices) { 

		//initializing char array of same length of indices array 
		char[] charArray = new char[indices.length];

		//iterate over indices and get the corresponding character from String 'S'
		for(int i =0 ;i < indices.length ;i++)
			charArray[indices[i]] =  s.charAt(i);

		//create new string wit charArray as arg(convert char array to string)
		return new String(charArray);
	}
}