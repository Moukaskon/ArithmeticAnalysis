#include<stdio.h>
#include<math.h>
#include<string.h>

double func(double x);

int main(){
    double a = 1;
    double b = 2;
    double e = 0.0001;
    double x = -1;
    double result;

    while(b - a > e){
        x = (a + b) / 2.0;
        result = func(x);
        if(result == 0){
            break;
        }else if(func(b) * result < 0){
            a = x;
        }else if(func(a) * result < 0){
            b =x;
        }
    }
    printf("%.4f",  x);


return 0;
}


double func(double x){
    return pow(x, 2) - 3;
}
