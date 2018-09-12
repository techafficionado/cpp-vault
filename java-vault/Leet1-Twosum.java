/*Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
*/
class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hmap = new HashMap<Integer, Integer>();
        int[] resarr=new int[2];
        for(int i=0;i<nums.length;i++){
            if (hmap.containsKey(target-nums[i])){
                System.out.println("num1: " +nums[i]+ " nums2:"+ hmap.get(nums[i]));                
                resarr[0]=hmap.get(target-nums[i]);
                resarr[1]=i;
            }
            else{
                hmap.put(nums[i],i);
            }
        }
        
        for(int k:hmap.keySet()){
            System.out.println("Key:"+k+" Value:"+hmap.get(k));
        }
        return resarr;
    }
}
