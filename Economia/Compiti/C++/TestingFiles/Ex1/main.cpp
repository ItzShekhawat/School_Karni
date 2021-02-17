#include <iostream>
using namespace std;

class Operator{

    private:
        string op;

    public:
        Operator(string op){
            if(op != "+"){ cout << " Operator not valid" << endl; op = "+"; }
            else{ op = op; }
        }

        virtual void adding() = 0;


};

class Num : public Operator{



};

class Str : public Operator{




};
// ----------------------------------------------------------------------------------

int main(){

    string val1;
    string val2;
    string operation;


    cout << "Welcom to the c++ manupulation file" << endl;

    cout << "Please enter your first element: " << endl;
    cin >> val1;

    cout << "Please enter your second element: " << endl;
    cin >> val2;

    cout << "Please enter the operator : " << endl;
    cin >> operation;


    // ----------------------------------------------------------------



    return 0;
}
