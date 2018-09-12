class Solution {
public:
    void swap(char *a, char *b){
	char x = *a;
	*a = *b;
	*b = x;
    }
    
    string reverseString(string s) {
        int low = 0;
        int high = s.length()-1;
        while(high>low){
            //std::cout << "high:" << high << " low:" << low << std::endl;
            swap(&s[low],&s[high]);
            low++;
            high--;
        }
        return s;
    }
};
