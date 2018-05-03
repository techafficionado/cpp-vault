class Solution {
    public int reverse(int x) {
        int revnum = 0;
        int tempx = x;
        int revnumshadow = 0;
        if(tempx<0){
            tempx = -1*tempx;
        }
        while(tempx>0){
            revnumshadow = revnum;
            revnum = revnum*10 + (tempx%10);
            if ((revnum - tempx%10)/10 !=revnumshadow) // reversing the above computation should result in the same number, if it does not then wraparound happened which means the number was large than [-2^31,2^31-1]
                return 0;
            tempx = tempx/10;
        }
        //System.out.println("revnum: "+revnum);
        //if (x>0 && revnum>2147483647){
        //    return 0;
        //}
        if (x<0){
            revnum = -1*revnum;
            //if (revnum < -2147483647)
            //    return 0;
        }
        return revnum;    
    }
}
