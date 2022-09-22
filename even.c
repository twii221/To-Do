#include<stdio.h>

int main(){
    int a;
    printf("\n Enter any number");
    scanf("%d",&a);
    
    if (a%2==0)
    {
        printf("\n Entered number is even");
    }
    else
    {
         printf("\n Entered number is odd");
    }
    return 0;
}