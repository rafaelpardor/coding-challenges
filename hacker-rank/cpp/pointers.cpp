#include<stdio.h>
#include<iostream>

void update(int *a, int*b){
}

int main(){
  int a, b;
  int *pa = &a;
  int *pb = &b;

  update(pa, pb);

  return 0;
}
