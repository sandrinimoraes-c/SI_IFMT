#include <stdio.h>
#include <stdlib.h>

typedef struct Celula {
    int valor;
    struct Celula *prox;
} Celula;

typedef struct {
    Celula *cabeca;   // célula cabeça (não guarda valor)
    int tam;
} Lista;

void inicia(Lista *l) {
    l->cabeca = malloc(sizeof(Celula));
    l->cabeca->prox = NULL;
    l->tam = 0;
}

void insereFim(Lista *l, int v) {
    Celula *p = l->cabeca;
    while (p->prox != NULL) p = p->prox;
    Celula *n = malloc(sizeof(Celula));
    n->valor = v;
    n->prox = NULL;
    p->prox = n;
    l->tam++;
}

void imprime(Lista *l) {
    for (Celula *p = l->cabeca->prox; p != NULL; p = p->prox)
        printf("%d ", p->valor);
    printf("\n");
}

/* Questão 1: retorna 1 se o valor está na lista, 0 caso contrário */
int estaNaLista(Lista *l, int valor) {
    Celula *p = l->cabeca->prox;
    while (p != NULL) {
        if (p->valor == valor) return 1;
        p = p->prox;
    }
    return 0;
}

/* Questão 2: troca os elementos das posições i e j (0 = primeiro elemento) */
int troca(Lista *l, int i, int j) {
    if (i < 0 || j < 0 || i >= l->tam || j >= l->tam) return 0;
    Celula *a = l->cabeca->prox, *b = l->cabeca->prox;
    for (int k = 0; k < i; k++) a = a->prox;
    for (int k = 0; k < j; k++) b = b->prox;
    int aux = a->valor;
    a->valor = b->valor;
    b->valor = aux;
    return 1;
}

int main() {
    Lista l;
    inicia(&l);
    for (int i = 1; i <= 5; i++) insereFim(&l, i * 10);
    printf("Lista: ");  imprime(&l);
    printf("estaNaLista(30) = %d\n", estaNaLista(&l, 30));
    printf("estaNaLista(99) = %d\n", estaNaLista(&l, 99));
    troca(&l, 0, 4);
    printf("Apos troca(0,4): "); imprime(&l);
    return 0;
}
