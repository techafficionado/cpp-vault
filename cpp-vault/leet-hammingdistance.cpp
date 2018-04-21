class Solution {
public:
    int hammingDistance(int x, int y) {
        int res = x ^ y;
        //std::cout << "res: " << res << std::endl;
        int hamdist = 0;
        int is1 = 0;
        while(res>0){
            is1 = res&1;
            hamdist = hamdist + is1;
            //std::cout << "hamdist:" << hamdist << endl;
            res = res >> 1;
        }
        //std::cout << "res: " << res << std::endl;
        return hamdist;
    }
};
