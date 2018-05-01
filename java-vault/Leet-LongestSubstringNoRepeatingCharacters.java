import java.util.HashMap;
import java.lang.Math;
//eg: abcabcd answer = 4
//eg: tmmzuxt answer = 5
class Solution {
    public int lengthOfLongestSubstring(String s) {
        char[] sarr = s.toCharArray();
        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        //HashMap<String, int> map = new HashMap<String, int>();
        int start = 0;
        int maxlen = 0;
        for(int i=0;i<sarr.length;i++){
            if (map.containsKey(sarr[i]) && start <= map.get(sarr[i])){                    
                start = map.get(sarr[i])+1;
                //System.out.println("Map Contains sarr[i]:"+sarr[i]+" start:"+start);
            }
            else{             
                //System.out.println("sarr[i]:"+sarr[i]); 
                //System.out.println("maxlen:"+maxlen+" start:"+start+" i:"+i);
                maxlen = Math.max(maxlen, (i-start+1));                
            }
                
            map.put(sarr[i],i);
            //System.out.println(Arrays.asList(map));   
            //if (map.containsValue('a'))
            //    System.out.println("Value present");
        }
        return maxlen;
    }
}
