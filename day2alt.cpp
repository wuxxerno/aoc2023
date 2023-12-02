#include <iostream>

#include <fstream>

#include <string>

#include <string.h>

using namespace std;

typedef struct set {
  int rgb[3];
  bool use;
}
set;

// Ascii decimal values for r, g, b "," ";"
/*We wont look for the complete words but just the 
first letter and the data delimitors for colors and sets
*/
const int red = 114;
const int green = 103;
const int blue = 98;
const int comma = 44;
const int semicolon = 59;
const int space = 32;

bool is_digit(int num) {
  //Returns wether a character is in the ascii number range
  return num >= 48 && num <= 57;
}

//Statekeeping
int current_set = 0;
int current_color_idx = 0;
int current_state = 0;
int current_digit_placement = 0;
char color_count_digits[6] = {
  48
};
int set_index = 0;

set sets[10] = {
  0
};

int line_nr = 1;

int main() {

    int sum = 0;

    string line;
    ifstream f("data");
    memset(color_count_digits, 0, 6);

    while (getline(f, line)) {
      int start = line.find(":");

      for (int i = 0; i < 10; i++) {
        sets[i].rgb[0] = 0;
        sets[i].rgb[1] = 0;
        sets[i].rgb[2] = 0;
        sets[i].use = 0;
      }

      int line_length = line.length();
      // Begin at 8 to skip Game n: 
      bool last_was_space = 0;
      set_index = 0;
      for (int i = start + 1; i < line_length; i++) {
        //cout << "line" << line_nr;
        bool do_color = 0;
        bool bump_set = 0;
        switch (line[i]) {

        case red:
          if (last_was_space) {
            current_color_idx = 0;
            last_was_space = 0;
          }

          break;
        case green:
          if (last_was_space) {
            current_color_idx = 1;
            last_was_space = 0;
          }
          break;
        case blue:
          if (last_was_space) {
            current_color_idx = 2;
            last_was_space = 0;
          }
          break;
        case space:
          //flag to only read the first letter if the previous character was space
          //otherwise the R in green would trigger red for example.
          last_was_space = 1;
          break;
        case comma:
          do_color = 1;
          break;
        case semicolon:
          do_color = 1;
          bump_set = 1;
          break;
        default:
          if (is_digit(line[i])) {
            sets[set_index].use = 1;
            color_count_digits[current_digit_placement] = line[i];
            current_digit_placement++;
          } else {
            current_digit_placement = 0;
          }
          break;
        }

        if (do_color || i == line_length - 1) {
          sets[set_index].rgb[current_color_idx] += atoi(color_count_digits);
          memset(color_count_digits, 0, 6);
          current_digit_placement = 0;
        }
        if (bump_set) {
          set_index++;
        }
      }

      int largest_r = 0;
      int largest_g = 0;
      int largest_b = 0;

      for (int i = 0; i < 10; i++) {

        if (sets[i].use) {

          if (sets[i].rgb[0] > largest_r) {
            largest_r = sets[i].rgb[0];
          }
          if (sets[i].rgb[1] > largest_g) {
            largest_g = sets[i].rgb[1];
          }
          if (sets[i].rgb[2] > largest_b) {
            largest_b = sets[i].rgb[2];
          }
        }
      }
        sum += largest_r * largest_g * largest_b;

        line_nr++;
      }
      cout << "sum:" << sum;
      f.close();
    
      return 0;
}