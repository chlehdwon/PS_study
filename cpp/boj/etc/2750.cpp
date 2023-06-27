#include <iostream>
# define SWAP(x, y, temp) ( (temp)=(x), (x)=(y), (y)=(temp) )
using namespace std;

void quick_sort(int *list, int left, int right);
int partitions(int *list, int left, int right);

int main(){
	ios::sync_with_stdio(false);
    cin.tie(0);
	
	int n;
	cin >> n;
	int *list = new int[n];
	for(int i=0; i<n; ++i){
		cin >> list[i];
	}
	quick_sort(list, 0, n-1);
	for(int i=0; i<n; ++i){
		cout << list[i] << "\n";
	}
	delete[] list;
	
	return 0;
}


int partitions(int *list, int left, int right){
  int pivot, temp;
  int low, high;

  low = left+1;
  high = right;
  pivot = list[left];
  while(low<=high){
	while(low<=right && list[low]<pivot) low++;
	while(high>left && list[high]>pivot) high--;
	if(low<=high) SWAP(list[low], list[high], temp);
	else SWAP(list[left], list[high], temp);
  }

  return high;
/*
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
*/
}

void quick_sort(int *list, int left, int right){
  if(left<=right){
    int q = partitions(list, left, right);
    quick_sort(list, left, q-1);
    quick_sort(list, q+1, right);
  }
}