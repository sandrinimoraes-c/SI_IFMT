#include <stdio.h>

int main() {
    int soma = 0;

    for (int i = 1; i <= 100; i++) {
        soma += i;
    }

    printf("Soma: %d\n", soma);
    return 0;
}

//Complexidade: O(n), com n = 100 (poderia ser calculado em O(1) usando a fórmula n(n+1)/2, mas a versão iterativa é O(n)).