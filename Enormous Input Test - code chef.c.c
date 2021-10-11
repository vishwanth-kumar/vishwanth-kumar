#include<stdio.h>
int main()
{
	int t,k,count=0;;
	scanf("%d",&t);
	scanf("%d",&k);
	for(int i=0;i<t;i++)
	{
		printf("#test case %d\n",i);
	    int n;
		scanf("%d",&n);
			if(n%k==0)
		{
			count++;
		}
	}
	printf("%d",count);
		return 0;
}