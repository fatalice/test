#include <stdio.h>

char a[20][20];

void matrix(int n)
{
	int A=0,B=n;
	char c='#';
	for(int k=0; k<n; k++){
		for(int i=A;i<B;i++){
			for(int j=A;j<B;j++){
				if(i==A || i==B-1){
					a[i][j]=c;
				}else{
					if(j==A || j==B-1){
						a[i][j]=c;
					}	
				}
			}
		}
		A++;
		B--;
		if(A==1){
			c='*';
		}else{
			c=46+A;
		}
	}
}

void print(int n)
{
	matrix(n);
	for(int i=0; i<n; i++){
		for(int j=0; j<n; j++){
			printf("%c", a[i][j]);
		}
		printf("\n");
	}
}

int main()
{
	int n;
	printf("Please input a number: (3<=n<=20)");
	scanf("%d", &n);
	print(n);
	return 0;
}

