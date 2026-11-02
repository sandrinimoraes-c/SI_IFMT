#include <stdio.h>

int ehPerfeito(int n) {
    int soma = 0;
    for (int i = 1; i < n; i++) {
        if (n % i == 0) soma += i;
    }
    return soma == n;
}

int main() {
    int x;
    printf("Digite um numero: ");
    scanf("%d", &x);

    if (ehPerfeito(x))
        printf("%d e perfeito\n", x);
    else
        printf("%d nao e perfeito\n", x);

    return 0;
}

//Complexidade: O(n) — percorre todos os divisores possíveis de 1 até n-1.