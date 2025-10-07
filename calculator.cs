#include <iostream>
using namespace std;

int main() {
    while (true) {
        int a, b;
        char islem;

        cout << "----------CALCULATOR----------\n";
        cout << "Write first number: ";
        cin >> a;
        cout << "Write second number: ";
        cin >> b;
        cout << "Select the action you want to perform (+,-,*,/): ";
        cin >> islem;

        switch (islem) {
            case '+': cout << "result: " << a + b << endl; break;
            case '-': cout << "result: " << a - b << endl; break;
            case '*': cout << "result: " << a * b << endl; break;
            case '/': cout << "result: " << (float)a / b << endl; break;
            default: cout << "invalid transaction\n";
        }
        cout << "action completed.\n\n";
    }
    return 0;
}
