#include <stdio.h>

#define N 7   // tamanho do vetor A
#define K 9   // maior valor possível (alcance: 0 até 9)

void imprimir(const char *nome, int v[], int tam) {
    printf("%s = ", nome);
    for (int i = 0; i < tam; i++)
        printf("%d ", v[i]);
    printf("\n");
}

int main(void) {
    int A[N] = {1, 4, 1, 2, 7, 5, 2};
    int B[N];        // vetor ordenado
    int C[K + 1];    // vetor de contagem (posições 0 até K)
    int i, j;

    imprimir("A", A, N);

    // 1. Zera o vetor C
    for (i = 0; i <= K; i++)
        C[i] = 0;

    // 2. Conta quantas vezes cada valor aparece
    for (j = 0; j < N; j++)
        C[A[j]] = C[A[j]] + 1;
    imprimir("C (contagem)", C, K + 1);

    // 3. Atualiza C com a soma acumulada
    for (i = 1; i <= K; i++)
        C[i] = C[i] + C[i - 1];
    imprimir("C (acumulado)", C, K + 1);

    // 4. Monta B, percorrendo A da direita para a esquerda
    for (j = N - 1; j >= 0; j--) {
        C[A[j]] = C[A[j]] - 1;
        B[C[A[j]]] = A[j];
    }
    imprimir("B (ordenado)", B, N);

    return 0;
}