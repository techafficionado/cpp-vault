//Write a program that outputs the string representation of numbers from 1 to n.
//But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string> svec;
        svec.push_back("1");
        for(int i=2;i<=n;i++){
            std::string val = std::to_string(i);
            if(!(i%3==0) && !(i%5==0)){
               svec.push_back(val);
            }
            else{
                val = "";
                if (i%3==0)
                    val = "Fizz";
                if (i%5==0)
                    val += "Buzz";
                svec.push_back(val);
            }
        }
        return svec;
    }
    
};
