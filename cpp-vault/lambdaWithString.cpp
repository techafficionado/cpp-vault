#include <iostream>
#include <algorithm>
#include <functional>
using namespace std;

int main() {
	// your code goes here
	std::string s = "anagram";
	std::sort(s.begin(),s.end());
	
	std::cout << "s:" << s << std::endl;
	
	s = "anagram";
	std::sort(s.begin(),s.end(),std::less<char>());
	std::cout << "s1:" << s << std::endl;
	
	std::sort(s.begin(),s.end(),[](char a, char b){return a>b;});
	std::cout << "s1:" << s << std::endl;
	
	std::sort(s.begin(),s.end(),[](const char& lhs, const char& rhs){return lhs > rhs;});
	std::cout << "s2:" << s << std::endl;
	return 0;
}
