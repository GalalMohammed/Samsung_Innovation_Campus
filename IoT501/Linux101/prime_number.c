#include <stdio.h>

int main(){
	int x;
	char flag = 1;

	printf("Enter x: ");
	scanf("%d", &x);
	for (int i = 2; i * i <= x; i++)
	{
		if (x % i == 0)
		{
			flag = 0;
			break;
		}
	}
	if (flag && x > 1)
		printf("It's a prime number.\n");
	else
		printf("It isn't a prime number.\n");
	return (0);
}
