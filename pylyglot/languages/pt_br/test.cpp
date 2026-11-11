#include <string>
#include <iostream>

void main(){
    int *i = 0;
    std::cout << "Teste" << std::endl;
    if (*i == 0) {
        i++;
    } else {
        i--;
    }
    return;
}