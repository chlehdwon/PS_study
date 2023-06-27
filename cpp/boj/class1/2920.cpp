#include <cstdio>
#include <cstring>

int main(){
	char nums[16];
	fread(nums, 1, 16, stdin);
	switch(nums[0]){
		case '1':
			for(int i=1; i<=8; i++){
				if((int)nums[2*i-2]-(int)'0' != i){
					printf("mixed\n");
					return 0;
				}
			}
			printf("ascending\n");
			break;
		case '8':
			for(int i=8; i>0; i--){
				if((int)nums[16-2*i]-(int)'0'!=i){
					printf("mixed\n");
					return 0;
				}
			}
			printf("descending\n");
			break;
		default:
			printf("mixed\n");
			break;
	}

	return 0;
}