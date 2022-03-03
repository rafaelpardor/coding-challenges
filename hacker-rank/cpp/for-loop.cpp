#include <iostream>

int main() {
  std::string string_arr[] = {"","one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
  int a;
  int b;
  std::cin >> a >> b;

  for(int i=a;i<=b;i++) {
      if (i <= 9){
        std::cout << string_arr[i] << "\n";
      } else if (i%2 == 0) {
        std::cout << "even" << "\n";
      } else if (i % 2 != 0){
        std::cout << "odd" << "\n";
      }
  }

  return 0;
}
