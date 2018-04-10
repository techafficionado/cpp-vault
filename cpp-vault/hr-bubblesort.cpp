#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

void swap(int &i, int &j){
    int tmp = 0;
    tmp = i;
    i = j;
    j = tmp;
}


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int n=0;
    cin >> n;
    std::vector<int> svec(n);
    int swaps = 0;
    for(int i=0;i<n;i++)
        cin >> svec[i];
    for(int i=0;i<n;i++){
        for(int j=0;j<n-i-1;j++){
            if (svec[j] > svec[j+1]){
                swap(svec[j],svec[j+1]);
                swaps++;
            }
        }
    }
    cout << "Array is sorted in " << swaps << " swaps." << endl;
    cout << "First Element: " << svec[0] << endl;
    cout << "Last Element: " << svec[n-1] << endl;
    /*
    for(auto x:svec)
        cout << "x:" << x << endl;
        */
    return 0;
}
