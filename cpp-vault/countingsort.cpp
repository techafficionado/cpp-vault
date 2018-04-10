#include <iostream>
#include <algorithm>


void printvec(std::vector<int> vec){
    for(auto &i:vec)
        std::cout << i << "\t";

    std::cout << "\n";
}

int main(){
    std::vector<int> vec = {1, 4, 1, 2, 7, 5, 2};
    std::vector<int> carr(10);
    std::vector<int> newarr(10);
    int elem = 0;
    for(int i=0;i<vec.size();i++){
        elem = vec[i];
        std::cout << "element: " << elem << std::endl;
        carr[elem]++;
    }

    std::cout << "printing carr" << std::endl;

    printvec(carr);

    for(int i=1;i<carr.size();i++){
        carr[i] = carr[i-1] + carr[i];
    }

    std::cout << "printing carr 1: " << std::endl;

    printvec(carr);

    int carrelem = 0;
    for(int i= vec.size()-1; i>=0; i--){
        elem = vec[i];
        carrelem = carr[elem];
        std::cout << "element: " << elem << " carr: " << carrelem <<std::endl;
        newarr[carrelem] = elem;
        carr[elem]--;
    }

    std::cout << "printing newarr" << std::endl;

    printvec(newarr);
}

