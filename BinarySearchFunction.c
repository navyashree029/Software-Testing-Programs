#include<stdio.h>
int binsrc(int x[],int low,int high,int key)
{
    int mid;
    while(low<=high)
    {
        mid=(low+high)/2;
        if(x[mid]==key)
        return mid;
        if(x[mid]<key)
        low=mid+1;
        if(x[mid]>key)
        high=mid-1;
    }
    return -1;
}

int main()
{
int key,i ,n,succ,a[20];
printf("Enter the size of the array");
scanf("%d",&n);


if(n>0)
{
    printf("Enter the n elements");
    for(i=0;i<n;i++)
    scanf("%d",&a[i]);
   
    printf("Enter the key element to be searched");
    scanf("%d",&key);
    succ=binsrc(a,0,n-1,key);
    if(succ>=0)
    printf("Element is found in position %d",succ+1);
    else
    printf("Elememt not found");
}
else
printf("Number of elements shud b greater than zero");
return 0;
}