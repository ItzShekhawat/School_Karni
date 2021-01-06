#include <iostream>
using namespace std;

int main(){
    cout << "Main started";
    // Variables 
    int shift_num;
    long index;
    string message;
    string message_encrypted;
    string the_alphabet_key = "ABCDEFGHILMNOPQRSTUVZ";

    // Request of the message ----------------------
    cout << "Give the message (cap letters): \n";
    cin >> message;
    int length = message.length();
        // Uppercase every char
    for (int k = 0; k < length; k++){
        message[k] = toupper(message[k]);
    }
    cout << "\nThe message is : " << message ;
    // ---------------------------------------------

    // Asking the shift number----------------------
    cout << " \nGive the shift number :";
    cin >> shift_num;
    cout << "\nThe shift number is : " << shift_num;
    // ---------------------------------------------


    // Checking the shift number 
    if (shift_num > 0){
        for(int i = 0; i < length; i++){
            index = the_alphabet_key.find(message[i]);
            for(int k = 0; k < shift_num; k++){

                index++;

                if(index == the_alphabet_key.length() + 1) index = 0;
            }

            message_encrypted += the_alphabet_key[index];
        }

    }else{
        for(int i = 0; i < length; i++){
            index = the_alphabet_key.find(message[i]);
            for(int k = 0; k > shift_num; k--){
                index--;

                if(index == -1) index = the_alphabet_key.length()-1;
            }

            message_encrypted += the_alphabet_key[index];
        }

    }

    cout << "\nmessage Encrypted: " << message_encrypted << "\n";

    return 0;
}


