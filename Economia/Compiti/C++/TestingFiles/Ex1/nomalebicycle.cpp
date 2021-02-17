#include <iostream>
using namespace std;

class nomalebicycle{
    private:
        string color;
        string height;
        string model;

    void init(string color, string height, string model){
        color = color;
        height = height;
        model = model;
    }

    string getColor(){
        cout << "The color of this bicycle is " << color << endl;
    }

    string toString(){
        cout << "The information about this bicycle are color : " << color << "\n model : " << model << "height : " << height << endl;    
    }

}