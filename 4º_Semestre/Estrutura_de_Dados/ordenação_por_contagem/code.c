#include <stdio.h>   // biblioteca com o printf (mostrar na tela)

#define N 7   // N = quantidade de elementos do vetor A
#define K 9   // K = maior valor possivel (alcance: de 0 ate 9)

// Funcao auxiliar: mostra um vetor na tela com o nome na frente.
// Nao faz parte do algoritmo, serve so para acompanhar cada etapa.
void imprimir(const char *nome, int v[], int tam) {
    printf("%s = ", nome);
    for (int i = 0; i < tam; i++)
        printf("%d ", v[i]);
    printf("\n");
}

int main(void) {
    int A[N] = {1, 8, 1, 2, 7, 5, 2};   // A = vetor de entrada (desordenado)
    int B[N];                           // B = vetor de saida (ficara ordenado)
    int C[K + 1];                       // C = vetor de contagem (posicoes 0 ate K)
    int i, j;                           // i percorre o C | j percorre o A

    imprimir("A", A, N);                // mostra o vetor original

    // PASSO 1: zerar o vetor C
    // Percorre todas as posicoes de C (de 0 ate K) e coloca 0.
    // Necessario, pois em C a memoria nao inicializada tem lixo.
    for (i = 0; i <= K; i++)
        C[i] = 0;

    // PASSO 2: contar quantas vezes cada valor aparece
    // O valor lido de A vira o INDICE de C: se leio um 4, somo 1 em C[4].
    // No fim, C[x] = quantidade de vezes que x aparece em A.
    for (j = 0; j < N; j++)
        C[A[j]] = C[A[j]] + 1;
    imprimir("C (contagem)", C, K + 1);

    // PASSO 3: soma acumulada
    // Cada posicao de C soma com a anterior (comeca em 1, pois nao existe C[-1]).
    // No fim, C[x] = quantidade de elementos MENORES OU IGUAIS a x,
    // ou seja, indica onde termina o grupo do valor x no vetor ordenado.
    for (i = 1; i <= K; i++)
        C[i] = C[i] + C[i - 1];
    imprimir("C (acumulado)", C, K + 1);

    // PASSO 4: posicionar cada elemento em B
    // Percorre A da DIREITA para a ESQUERDA, o que mantem a ordem original
    // dos elementos iguais (algoritmo estavel).
    for (j = N - 1; j >= 0; j--) {
        C[A[j]] = C[A[j]] - 1;   // diminui 1: resultado = indice onde o elemento vai ficar
        B[C[A[j]]] = A[j];       // coloca o elemento em B nessa posicao
    }
    imprimir("B (ordenado)", B, N);     // mostra o resultado final

    return 0;   // fim do programa, sem erros
}