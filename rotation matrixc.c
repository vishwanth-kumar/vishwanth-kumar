#include<stdio.h>
int main()
{
    int n,a[100][100],c[100][100],i,j,m,t;
    scanf("%d",&t);
    while(t--)
    {
         scanf("%d",&n);
         scanf("%d",&m);
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=m;j++)
        {
            scanf("%d",&a[i][j]);
        }
        printf("\n");
    }
    for(int i=1;i<=n;i++)
    {
        for(int j=m;j>=1;j--)
        {
            printf("%d ",a[i][j]);
        }
        printf("\n");
    }
     for(int i=n;i>=1;i--)
    {
        for(int j=1;j<=m;j++)
        {
            c[i][j]=a[j][i];
            printf("%d ",c[i][j]);
        }
        printf("\n");
    }
    }
    return 0;
}
