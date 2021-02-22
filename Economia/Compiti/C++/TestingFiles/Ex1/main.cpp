#include <iostream>
#include <cmath>
using namespace std;

class Operator{

    private:
        string op;

    public:
        Operator(string op){
            if(op != "+"){ cout << " Operator not valid" << endl; op = "+"; }
            else{ op = op; }
        }

        virtual void somma(){
            cout << "The onw" << endl;
        }


};

class Num : public Operator{

    void somma(float val1, float val2){
        cout << val1+val2 << endl;
    }

};

class Str : public Operator{
    
    void somma(string val1, string val2){

        cout << val1+val2 << endl;
    }

};
// ----------------------------------------------------------------------------------

int main(){

    float val1;
    float val2;
    string operation;


    cout << "Welcom to the c++ manupulation file" << endl;

    cout << "Please enter your first element: " << endl;
    cin >> val1;

    cout << "Please enter your second element: " << endl;
    cin >> val2;

    cout << "Please enter the operator : " << endl;
    cin >> operation;


    // ----------------------------------------------------------------

    Operator *op;
    Num n;
    op = &n;

    op->somma();


    return 0;
}
