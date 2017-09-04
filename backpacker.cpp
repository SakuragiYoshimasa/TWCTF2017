#include<iostream>
#include<string>

using namespace std;

int main(int argc, char const *argv[]) {

  string input;
  int ret = system("nc backpacker.chal.ctf.westerns.tokyo 39581");

  while(input.find("Input")){
      cin >> input;
      cout << input;
  }

  while(true){
    std::cout << "testsefs" << '\n';
  }

  return 0;
}
