#include <iostream>
#include <cmath>

int main(){
	int start, end;
	int square = -1;
	int sum = 0;
	std::cin >> start;
	std::cin >> end;
	for(int i=start; i<=end; i++){
		if(sqrt(i)==(int)sqrt(i)){
			if(square == -1) square = i;
			sum += i;
		}
	}
	if(square != -1) std::cout << sum << "\n";
	std::cout << square << std::endl;
	return 0;
}