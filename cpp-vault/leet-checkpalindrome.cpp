class Solution {
public:
    bool isPalindrome(string s) {
        int low = 0;
        int high = s.length()-1;
        std::transform(s.begin(),s.end(),s.begin(),::tolower);
        /*
        s.erase(std::remove(s.begin(),s.end(),[](char a){
                                                return (!isalnum(a) || isspace(a));
                                                }), s.end());
                                                */
        while(low<high){
            if(!isalnum(s[low]) || (isspace(s[low]))){
                low++;
                continue;
            }
            if(!isalnum(s[high]) || (isspace(s[low]))){
                high--;
                continue;
            }
            //std::cout << s[low] << " " << s[high] << std::endl;
            if (s[low] == s[high])
            {
                low++;
                high--;
            }
            else
                return false;
        }
        return true;
    }
};
