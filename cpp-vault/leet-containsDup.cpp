class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        std::unordered_map<int,int> smap;
        for(auto &x:nums){
            if(smap.count(x)<=0){
                smap[x] = 1;
            }
            else
            {
                //element already present in the map
                return true;
            }
        }
        return false;
    }
};
