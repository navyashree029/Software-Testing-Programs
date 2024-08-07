#include <stdio.h>

int main() {
    int a,b,c,c1,c2,c3;
    char istriangle;
    do{
        printf("Enter the 3 sides of a triangle");
        scanf("%d%d%d",&a,&b,&c);
        printf("a=%d,b=%d,c=%d",a,b,c);
        c1=a>=1&&a<=10;
        c2=b>=1&&b<=10;
        c3=c>=1&&c<=10;
        if(!c1)
        printf("a=%d does not lie in the range of permitted values",a);
        if(!c2)
        printf("b=%d does not lie in the range of permitted values",b);
        if(!c3)
        printf("c=%d does not lie in the range of permitted values",c);
}while(!(c1&&c2&&c3));
if (a<b+c&&b<a+c&&c<a+b)
istriangle='y';
else
istriangle='n';

if(istriangle=='y')
if((a==b)&&(b==c))
printf("Equilateral ");

else if(a!=b&&b!=c&&c!=a)
printf("Scalene triangle");
else
printf("Isoceles triangle");
else
printf("Not a triangle");
return 0;
}
