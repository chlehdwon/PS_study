#include <cstdio>

int main(){
	int index=-1, max=-1, num;
	for(int i=0; i<9; i++){
		scanf("%d", &num);
		if(max<num){
			index=i+1;
			max=num;
		}
	}
	printf("%d\n%d\n", max, index);
	
	return 0;
}

