#include <iostream>
#include <algorithm>
#include <string>


void printvec(std::vector<int> vec){
    for(auto &i:vec)
        std::cout << i << "\t";

    std::cout << "\n";
}

std::vector<int> csort(std::vector<int> vec){
    //std::vector<int> vec = {1, 4, 1, 2, 7, 5, 2};
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

    return newarr;
}

std::vector<int> csort1(std::vector<int> vec){
    //std::vector<int> vec = {1, 4, 1, 2, 7, 5, 2};
    std::vector<int> carr(10);
    std::vector<int> newarr(10);
    int elem = 0;
    for(int i=0;i<vec.size();i++){
        elem = vec[i];
        //std::cout << "element: " << elem << std::endl;
        carr[elem]++;
    }

    printvec(carr);

    for(int i=1;i<carr.size();i++){
        carr[i] = carr[i-1] + carr[i];
    }

    //std::cout << "printing carr 1: " << std::endl;

    printvec(carr);

    return carr;
    //int carrelem = 0;
    //for(int i= vec.size()-1; i>=0; i--){
    //    elem = vec[i];
    //    carrelem = carr[elem];
    //    std::cout << "element: " << elem << " carr: " << carrelem <<std::endl;
    //    newarr[carrelem] = elem;
    //    carr[elem]--;
    //}

    //std::cout << "printing newarr" << std::endl;

    //printvec(newarr);
    //
    //return newarr;
}
int main()
{

    std::vector<int> vec1 = {1, 4, 1, 2, 7, 5, 2};
    std::vector<int> nvec = csort(vec1);

    std::cout << "printing newarr" << std::endl;

    printvec(nvec);

    //std::vector<int> vec = {28,22,24,21,10,50,29};
    std::vector<int> vec = {228,422,324,821,910,250,4429};

    // get length of max element
    int len = std::to_string(*std::max_element(vec.begin(),vec.end())).length();

    std::cout << "len: " << len << std::endl;

    // single digit temporary vector
    std::vector<int> tempvec(vec.size());
    // count sum array
    std::vector<int> carr(10);
    // final temporary arry
    std::vector<int> newarr(10);
    int carrelem = 0;
    int elem = 0;
    for(int i = 0; i < len; i++)
    {
        for (int j=0;j<vec.size();j++)
            tempvec[j] = int(vec[j]/pow(10,i))%10;
        std::cout << "tempvec:" << std::endl;
        printvec(tempvec);
        carr = csort1(tempvec);
        for(int i= vec.size()-1;i>=0;i--){
            elem = tempvec[i];
            carrelem = carr[elem];
            std::cout << "element: " << elem << " carr: " << carrelem <<std::endl;
            newarr[carrelem] = vec[i];
            carr[elem]--;
        }
        std::cout << "newarr: " << std::endl;
        printvec(newarr);
        int l = 0;
        for(auto &v:newarr)
        {
            if (v!=0){
                vec[l] = v;
                l++;
            }
        }
        std::cout << "original vec: " << std::endl;
        printvec(vec);
    }
}

