import java.lang.String;
import java.util.Arrays;
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> smap = new HashMap<String, List<String>>();
        List<List<String>> lis = new ArrayList<List<String>>();
        char[] tempArray;
        String sortStr;
        for(String s: strs){
            //System.out.println("s:"+s);
            tempArray =  s.toCharArray();
            Arrays.sort(tempArray);
            sortStr = new String(tempArray);
            //System.out.println("sorStr:"+sortStr);
            //String sortStr = new String(Arrays.sort(s.toCharArray()));
            if (smap.containsKey(sortStr)){
                smap.get(sortStr).add(s);
            }
            else{
                smap.put(sortStr, new ArrayList<String>());
                smap.get(sortStr).add(s);
            }
        }
        
        
        for (String key : smap.keySet()){
            //iterate over key
            //System.out.println(key+" "+smap.get(key));
            lis.add(smap.get(key));
        }
        return lis;
    }
}
