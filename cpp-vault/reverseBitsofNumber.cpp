class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        int is1 = 0;
        int size = 32;
        std::string myvec[size];
        int i = 0;
        int revnum = 0;
        while (n>0){
	    // check if each lsb is a 1
            is1 = n & 1;
            // if it is 1, do an or with 1 moved to the MSB and an or - which adds that 1 but in reverse position
            if (is1){
                revnum = revnum | (1<<(32-1)-i);
            }
            i++;
            n = n >> 1;
        }
        
        std::cout << "revnum:" << revnum << "\n";
        
        return revnum;
    }
};
