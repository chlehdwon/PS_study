#include <cstdio>
# define SWAP(x, y, temp) ( (temp)=(x), (x)=(y), (y)=(temp) )

void quick_sort(int list[], int left, int right);
int partitions(int list[], int left, int right);
int binary_search(int list[], int target, int left, int right);

int main(){
	int n,m;
	int nums[100000]={0};
	int targets[100000]={0};
	scanf("%d", &n);
	for(int i=0; i<n; i++){
		scanf("%d", &nums[i]);
	}
	
	quick_sort(nums, 0, n-1);
	
	scanf("%d", &m);
	for(int j=0; j<m; j++){
		scanf("%d", &targets[j]);
	}
	
	
	for(int k=0; k<m; k++){
		printf("%d\n", binary_search(nums, targets[k], 0, n));
	}
	
	return 0;
}

int partitions(int list[], int left, int right){
  int pivot, temp;
  int low, high;

  low = left;
  high = right + 1;
  pivot = list[left];
  do{
    do {
      low++;
    } while (low<=right && list[low]<pivot);

    do {
      high--;
    } while (high>=left && list[high]>pivot);
    if(low<high){
      SWAP(list[low], list[high], temp);
    }
  } while (low<high);

  SWAP(list[left], list[high], temp);

  return high;
}

void quick_sort(int list[], int left, int right){
  if(left<right){
    int q = partitions(list, left, right);
    quick_sort(list, left, q-1);
    quick_sort(list, q+1, right);
  }

}

int binary_search(int list[], int target, int left, int right){
	if(left>right) return 0;

	int mid=(left+right)/2;

	if(list[mid]==target) return 1;
	else if(list[mid]<target) return binary_search(list, target, mid+1, right);
	else return binary_search(list, target, left, mid-1);
	
}
