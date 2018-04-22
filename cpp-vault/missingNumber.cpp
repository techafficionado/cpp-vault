class Solution {
public:
    // example input [3,0,1], since a 0 is included taking as 'size' should be okay
    int missingNumber(vector<int>& nums) {
        int nsize = nums.size();
        std::cout << "nsize:" << nsize << std::endl;
        int totalsum = (nsize+1)*(nsize)/2;
        int vecsum = 0;
        for(auto n:nums)
            vecsum += n;
        
        int misnum = totalsum - vecsum;
        return misnum;
    }
};
