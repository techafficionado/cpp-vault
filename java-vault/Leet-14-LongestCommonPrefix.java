/*
Input: ["flower","flow","flight"]
Output: "fl"
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
*/
class Solution {
    public String longestCommonPrefix(String[] strs) {
        if(strs == null || strs.length == 0)    
            return "";
        String shortest = strs[0];
        for(String str:strs){
            if (str.length() < shortest.length()){
                shortest = str;
            }
        }
        System.out.println("shortest:"+shortest);        
        int i = 0;
        while(i<shortest.length()){
            for(String str:strs){
                if(str.charAt(i) == shortest.charAt(i))
                    continue;
                else{
                    return shortest.substring(0,i);
                }                                    
            }
            i++;                       
        }
        return shortest.substring(0,i);
    }
}
