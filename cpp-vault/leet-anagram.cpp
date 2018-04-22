class Solution {
public:
    bool isAnagram(string s, string t) {
        /*std::unordered_map<char,int> smap;
        int idx = 0;
        for(int i=0;i<s.length();i++){
            std::cout << "s[i]:" << s[i] << std::endl; 
            idx = s[i]-'a';   
            std::cout << "idx:" << idx << std::endl;
            smap[idx]++;
        }
        
        for(auto &s:smap){
            std::cout << "s.first:" << s.first << "s.second:" << s.second << std::endl;
        }*/
        
        std::sort(s.begin(),s.end());
        std::sort(t.begin(),t.end());
        if(s==t)
            return true;
        else 
            return false;
            
        return true;
    }
};
