import java.lang.*;
class Solution {
    
    public int checkPalinLen(String s, int start, int end){
        while(start>=0 && end<s.length() && s.charAt(start) == s.charAt(end) ){
            start--;
            end++;
        }
        return end-start-1;
    }
    
    public String longestPalindrome(String s) {
        if(s.length() == 1)
            return s;
        if(s.length()==2 && s.charAt(0)==s.charAt(1))
            return s;
        int len1 = 0;
        int len2 = 0;
        int maxlen = 0;
        int start = 0;
        int end = 0;
        for(int i=1;i<s.length();i++){
                len1 = checkPalinLen(s, i , i);
                len2 = checkPalinLen(s, i, i+1);    
                maxlen = Math.max(len1, len2);
                if (maxlen> end-start){
                    start = i - (maxlen-1)/2;
                    end = i+maxlen/2;
                }
                System.out.println("i: " + i +"len1: " +len1+" len2:"+len2+" maxlen:"+maxlen); 
                
        }
        return s.substring(start,end+1);
    }
}
