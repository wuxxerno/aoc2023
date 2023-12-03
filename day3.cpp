#include <iostream>

#include <fstream>

#include <string>

#include <string.h>

using namespace std;

bool is_digit(int num) {
  //Returns wether a character is in the ascii number range
  return num >= 48 && num <= 57;
}

int main() {

  int sum = 0;

  string lines[1024];

  ifstream f("data");
  int lc = 0;
  
  int current_digit_placement = 0;
char digits[6] = {0};

            memset(digits, 0, 6);
  while (getline(f, lines[lc])) {
    lc++;
  }
bool num_valid = 0;
  for (int l = 0; l < lc; l++) {
    for (int i = 0; i < lines[l].length(); i++) {
        if (is_digit(lines[l][i])) {
            digits[current_digit_placement] = lines[l][i];
            current_digit_placement++;
            if (l < lc-1) { 
                if(lines[l+1][i] != 46) {
                    num_valid = 1;
                    cout << " FOUND 1";
                }
                if (i > 0){
                if(lines[l+1][i-1] != 46) {
                    num_valid = 1;
                    cout << " FOUND 2";
                }               
                }
                if (i < lines[l].length()-1){
                    if(lines[l+1][i+1] != 46) {
                    num_valid = 1;
                }           
                }
            }
            if (l > 0) {
                  if(lines[l-1][i] != 46) {
                    num_valid = 1;
                }
                if (i > 0){
                if(lines[l-1][i-1] != 46) {
                    num_valid = 1;
                }               
                }
                if (i < lines[l].length()-1){
                    if(lines[l-1][i+1] != 46) {
                    num_valid = 1;
                }           
                }              
            }
            
                if (i > 0){
                if(lines[l][i-1] != 46 && !is_digit(lines[l][i-1])) {
                    num_valid = 1;
                            cout << " FOUND 3";
                }               
                }
                if (i < lines[l].length()-1){
                    if(lines[l][i+1] != 46 && !is_digit(lines[l][i+1])) {
                    num_valid = 1;
                            cout << " FOUND 4";
                }           
                }
            
        }else {
        if(current_digit_placement != 0){
            if (num_valid){
            cout << " number:" << digits;
            sum += atoi(digits);
                
            }
            num_valid = 0;
            current_digit_placement = 0;
                      memset(digits, 0, 6);
        }
    } 
    }

  }
cout << "sum:" << sum;
  f.close();
}