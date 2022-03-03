#include<iostream>

int max_of_four(int a, int b, int c, int d){
  int max = a;
  int arr[4] = {a,b,c,d};

  for(int i = 0; i<4; i++) {
    if (max < arr[i]){
      max = arr[i];
    }
  }

  return max;
}

int main() {
  int ans = max_of_four(1,2,3,4);
  std::cout << ans << std::endl;
  return 0;
}
