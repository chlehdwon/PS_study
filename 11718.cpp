#include <iostream>
#include <string>
 
int main(){ 
    std::string str;
    while (true){
        getline(std::cin, str);
        if (str=="")
            break;
        std::cout << str << std::endl;
    } 
    return 0;
}