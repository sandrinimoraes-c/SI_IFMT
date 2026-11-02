#include <stdio.h>

int ehPerfeito(int n) {
    int soma = 0;
    for (int i = 1; i < n; i++) {
        if (n % i == 0) soma += i;
    }
    return soma == n;
}

int main() {
    int N, contador = 0, num = 1;

    printf("Digite N: ");
    scanf("%d", &N);

    printf("Primeiros %d numeros perfeitos: ", N);
    while (contador < N) {
        if (ehPerfeito(num)) {
            printf("%d ", num);
            contador++;
        }
        num++;
    }
    printf("\n");
    return 0;
}

//Complexidade: O(N · M), onde M é o valor do N-ésimo número perfeito — para cada candidato testado, 
//percorre-se todos os divisores possíveis (O(n) por chamada de ehPerfeito). 
//omo os números perfeitos são muito raros e grandes, esse algoritmo é bem ineficiente para N > 4 na prática.