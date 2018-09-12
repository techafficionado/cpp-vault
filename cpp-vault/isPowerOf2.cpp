#include <iostream>
using namespace std;

class Solution{
	public:
		bool isPowerOf2(int num){
			bool isPow = false;
			if (num == 0)
			   return isPow;
			isPow = !(num & (num-1));
			std::cout << "isPow:" << isPow << std::endl;
			return isPow;
		}
	
};

int main() {
	// your code goes here
	Solution sol;
	sol.isPowerOf2(5);
	sol.isPowerOf2(4);
	return 0;

}
