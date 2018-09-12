class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int singleone = INT_MIN;
        if(nums.size() == 1)
            return nums[0];
        //vector<int> myvec(nums.size());
        std::map<int,int> mmap;
        for(auto &n:nums){
            //if(mmap.count(n)>0){
            if (mmap.find(n)!=mmap.end()){
                mmap[n]++;
            }
            else{
                mmap[n] = 1;                
            }
        }
        
        
        for(auto x:mmap){
            if (x.second == 1)
                singleone = x.first;
        }
        return singleone;
    }
};
