#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

bool checkPrime(int n){
    if(n==1 )
        return false;
    if(n==2)
        return true;
    // O(root(n)) complexity
    // use ceil to include that number as well
    for(int i=2;i<=int(ceil(sqrt(n)));i++){
        if(n%i==0)
            return false;
    }
    return true;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int T;
    cin >> T;
    int n;
    for(int i=0;i<T;i++){
        cin >> n;
        if(checkPrime(n))
            cout << "Prime" << endl;
        else
            cout << "Not prime" << endl;
    }
    return 0;
}
}
