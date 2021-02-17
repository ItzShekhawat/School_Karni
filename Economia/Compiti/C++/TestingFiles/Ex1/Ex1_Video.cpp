#include <iostream>
using namespace std;


class Bicycle{
    public:
        string color;
        string height;
        string model;

    Bicycle(string Icolor, string Iheight, string Imodel){
        color = Icolor;
        height = Iheight;
        model = Imodel;
    }

    void getColor(){
        cout << "The color of this bicycle is " << color << endl;
    }

    void toString(){
        cout << "The information about this bicycle are color : " << color << "\n model : " << model << "height : " << height << endl;    
    }

};


int main(){

    cout << "Setting up the bicycle chart : " << endl;
    cout << "Normale bicycle:" << endl;

    Bicycle b1("Red", "6", "city");

    b1.getColor();


    
    

    
    return 0;
}