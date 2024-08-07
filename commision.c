#include<stdio.h>
int main()
{
    int locks,stocks,barrels,tlocks,tstocks,tbarrels,c1,c2,c3,temp;
    float lprice,sprice,bprice,sales,comm;
    lprice=45.0;
    sprice=30.0;
    bprice=25.0;
    tlocks=0;
    tstocks=0;
    tbarrels=0;
    printf("Enter the number of locks or -1 to exit");
    scanf("%d",&locks);
    while(locks!=-1)
    {
        c1=(locks<=0 ||locks>=70);
        printf("Enter the stocks and barrels");
        scanf("%d %d",&stocks,&barrels);
        c2=(stocks<=0 ||stocks>=80);
        c3=(barrels<=0 ||barrels>=90);
        if(c1)
        printf("Value of locks not in the range 1 to 70");
        else
        {
            temp=tlocks+locks;
            if(temp>70)
            printf("new total locks = %d ",locks);
            else
            tlocks=temp;
        }
        printf("Total locks=%d",locks);
        if(c2)
        printf("Value of stocks not in the range 1 to 80");
        else
        {
            temp=tstocks+stocks;
            if(temp>80)
            printf("new total stocks = %d ",stocks);
            else
            tstocks=temp;
        }
        printf("Total stocks=%d",stocks);
        if(c3)
        printf("Value of barrels not in the range 1 to 90");
        else
        {
            temp=tbarrels+barrels;
            if(temp>90)
            printf("new total barrels = %d ",barrels);
            else
            tbarrels=temp;
        }
        printf("Total barrels=%d",barrels);
        printf("Enter the number of lockr or -1 to exit");
        scanf("%d",&locks);
    }
    printf("total locks=%d\ntotal stocks=%d\ntotal barrels=%d\n",tlocks,tstocks,tbarrels);
    sales=lprice*tlocks+sprice*tstocks+bprice*tbarrels;
    printf("the total sales=%f\n",sales);
    if(sales>0)
    {
        if(sales>1800)
        {
            comm=0.10*1000;
            comm=comm+0.15*1800;
            comm=comm+0.20*(sales-1800);
        }
        else if(sales>1000)
        {
            comm=0.10*1000;
            comm=comm+0.15*(sales-1000);
        }
        else
        comm=0.10*sales;
        printf("The comm is=%f",comm);
    }
    else
    printf("There is no sales\n");
    return 0;
}