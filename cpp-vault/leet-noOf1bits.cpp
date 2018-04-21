class Solution {
public:
    int hammingWeight(uint32_t n) {
        int count = 0;
        int is1 =0;
        while(n>0){
            is1 = n & 1;
            count = count + is1;
            n = n>>1;
        }
        //std::cout << "count:" << count << std::endl;
        return count;
    }
};
