#include <unistd.h>
int factorial(int n) {
    if(n == 0 || n == 1) return 1;
    return n * factorial(n-1);
}
int main(){
    write(1, "Hello Bangladesh.\n", 18);

    int n = 5;
    int fact = factorial(n);
    char str[100];
    sprintf(str, "Factorial of %d is %d\n", n, fact);
    write(1, str, 22);

    return 0;
}