#include <iostream>

#include <fstream>

#include <string>

using namespace std;

bool is_digit(int num) {
  return num >= 48 && num <= 57;
}

int main() {
  string l;
  ifstream f("data");
  int fd = -1;
  int sd = -1;
  int sum = 0;
  while (getline(f, l)) {
    int fd = -1;
    int sd = -1;
    int ll = l.length();
    for (int i = 0; i < ll; i++) {
      if (fd == -1) {
        if (is_digit(l[i])) {
          fd = l[i];
        }
      }
      if (sd == -1) {
        if (is_digit(l[ll - i - 1])) {
          sd = l[ll - i - 1];
        }
      }
    }
    sum += ((fd - 48) * 10) + sd - 48;
  }
  f.close();
  cout << "sum:" << sum;
  return 0;
}