#include <stdio.h>
#include <stdlib.h>

/* Célula como na figura: linha, coluna, valor, ponteiro p/ direita (linha) e p/ baixo (coluna).
   Listas circulares com célula cabeça. Cabeças de linha/coluna têm linha/coluna = -1. */
typedef struct Celula {
    int linha, coluna;
    int valor;
    struct Celula *direita, *abaixo;
} Celula;

typedef struct {
    Celula *cabeca;
    int m, n;   // m linhas, n colunas
} Matriz;

Celula *novaCelula(int i, int j, int v) {
    Celula *c = malloc(sizeof(Celula));
    c->linha = i; c->coluna = j; c->valor = v;
    c->direita = c; c->abaixo = c;
    return c;
}

Matriz *criaMatriz(int m, int n) {
    Matriz *M = malloc(sizeof(Matriz));
    M->m = m; M->n = n;
    M->cabeca = novaCelula(-1, -1, 0);
    Celula *p = M->cabeca;
    for (int j = 0; j < n; j++) {          // cabeças de coluna (ligadas por "direita")
        Celula *c = novaCelula(-1, -1, 0);
        p->direita = c; p = c;
    }
    p->direita = M->cabeca;
    p = M->cabeca;
    for (int i = 0; i < m; i++) {          // cabeças de linha (ligadas por "abaixo")
        Celula *c = novaCelula(-1, -1, 0);
        p->abaixo = c; p = c;
    }
    p->abaixo = M->cabeca;
    return M;
}

Celula *cabLinha(Matriz *M, int i) {       // i de 1 a m
    Celula *p = M->cabeca;
    for (int k = 0; k < i; k++) p = p->abaixo;
    return p;
}
Celula *cabColuna(Matriz *M, int j) {      // j de 1 a n
    Celula *p = M->cabeca;
    for (int k = 0; k < j; k++) p = p->direita;
    return p;
}

int busca(Matriz *M, int i, int j) {
    Celula *h = cabLinha(M, i);
    for (Celula *p = h->direita; p != h; p = p->direita)
        if (p->coluna == j) return p->valor;
    return 0;
}

/* Insere (ou atualiza) o elemento (i,j). Valor 0 não é armazenado. */
void insere(Matriz *M, int i, int j, int v) {
    Celula *hl = cabLinha(M, i);
    Celula *ant = hl;
    while (ant->direita != hl && ant->direita->coluna < j) ant = ant->direita;
    if (ant->direita != hl && ant->direita->coluna == j) {   // já existe
        ant->direita->valor = v;
        return;
    }
    if (v == 0) return;
    Celula *hc = cabColuna(M, j);
    Celula *cant = hc;
    while (cant->abaixo != hc && cant->abaixo->linha < i) cant = cant->abaixo;
    Celula *nova = novaCelula(i, j, v);
    nova->direita = ant->direita;  ant->direita = nova;
    nova->abaixo = cant->abaixo;   cant->abaixo = nova;
}

void imprime(Matriz *M) {
    for (int i = 1; i <= M->m; i++) {
        for (int j = 1; j <= M->n; j++) printf("%5d ", busca(M, i, j));
        printf("\n");
    }
}

/* C = A + B */
Matriz *soma(Matriz *A, Matriz *B) {
    if (A->m != B->m || A->n != B->n) return NULL;
    Matriz *C = criaMatriz(A->m, A->n);
    for (int i = 1; i <= A->m; i++) {
        Celula *h = cabLinha(A, i);
        for (Celula *p = h->direita; p != h; p = p->direita)
            insere(C, i, p->coluna, p->valor);
        h = cabLinha(B, i);
        for (Celula *p = h->direita; p != h; p = p->direita)
            insere(C, i, p->coluna, busca(C, i, p->coluna) + p->valor);
    }
    return C;
}

/* C = A * B  (A é m x n, B é n x p) */
Matriz *multiplica(Matriz *A, Matriz *B) {
    if (A->n != B->m) return NULL;
    Matriz *C = criaMatriz(A->m, B->n);
    for (int i = 1; i <= A->m; i++) {
        Celula *ha = cabLinha(A, i);
        for (Celula *a = ha->direita; a != ha; a = a->direita) {
            int k = a->coluna;                    // percorre a linha k de B
            Celula *hb = cabLinha(B, k);
            for (Celula *b = hb->direita; b != hb; b = b->direita)
                insere(C, i, b->coluna, busca(C, i, b->coluna) + a->valor * b->valor);
        }
    }
    return C;
}

int main() {
    Matriz *A = criaMatriz(4, 4), *B = criaMatriz(4, 4);
    insere(A, 1, 1, 50);  insere(A, 2, 1, 10);  insere(A, 2, 3, 20);
    insere(A, 4, 1, -30); insere(A, 4, 3, -60); insere(A, 4, 4, 5);
    for (int i = 1; i <= 4; i++) insere(B, i, i, 1);   // identidade

    printf("A:\n");     imprime(A);
    Matriz *S = soma(A, B);
    printf("\nA + I:\n"); imprime(S);
    Matriz *P = multiplica(A, A);
    printf("\nA * A:\n"); imprime(P);
    return 0;
}
