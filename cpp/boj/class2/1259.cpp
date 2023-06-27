#include <cstdio>
#include <cstdlib>

void is_palindrome(int n);
int main(){
	int n;
	while(scanf("%d", &n)){
		if(n) is_palindrome(n);
		else break;
	}
	
	return 0;
}

void is_palindrome(int n){
	int *num=(int *)malloc(5*sizeof(int));
	int temp=n, left=0, right=0;
	do{
		num[right]=temp%10;
		temp/=10;
		right++;
	}while(temp);
	right--;
	while(left<=right){
		if(num[left]!=num[right]){
			printf("no\n");
			free(num);
			return;
		}
		left++;
		right--;
	}
	printf("yes\n");
	free(num);
	return;
}