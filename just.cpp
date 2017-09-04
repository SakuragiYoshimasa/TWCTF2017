

#include <iostream>
#include<string>
using namespace std;

int main(int argc, char const *argv[]) {
  //int ret = system("nc pwn1.chal.ctf.westerns.tokyo 12345");
  //string s;
  //while(s.find('?') == -1){
  //  cin >> s;
  //  cout << s << endl;
  //}
  cout << "FIN" << endl;
  if(strcmp("P@SSW0RD", "P@SSW0RD\n") == 0){
    cout << "same" << endl;
  }else{
    cout << "Diff" << endl;
  }
  return 0;
}
