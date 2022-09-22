#include<stdio.h>

int main(){
    int a,b,c,total;
    printf("\n Enter marks in math");
    scanf("%d",&a);
    printf("\n Enter marks in physics");
    scanf("%d",&b);
     printf("\n Enter marks in chem");
    scanf("%d",&c);
    total= a+b+c;
    printf("\n total is:%d",total);
   
    if (total>=190)
    {
        printf("\n Candidate is eligible for admission");
    }
    else
    {
         printf("\n Candidate is not eligible for admission");
    }
    return 0;
}