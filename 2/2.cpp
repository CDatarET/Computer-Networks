#include <iostream>
#include <cmath>
using namespace std;

int main(){
    cout << "Hello World\n";

    cout << "Enter Data: ";
    string data;
    cin >> data;

    int r = 0;
    while(pow(2, r) < data.length() + r + 1){
        r++;
    }

    int n = data.length() + r + 1;
    int code[n];
    for(int i = 0; i < data.length(); i++){
        code[n - 1 - (int)pow(2, i)] = (int)(data[i] - '0');
    }

    for(int i = 0; i < n - 1; i++){
        cout << code[i] << " ";
    }
    cout << endl;

    return 0;
}
