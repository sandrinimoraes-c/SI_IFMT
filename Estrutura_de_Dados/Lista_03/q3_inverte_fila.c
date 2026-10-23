#include <stdio.h>
#define MAX 100

typedef struct { int v[MAX]; int ini, fim, qtd; } Fila;
typedef struct { int v[MAX]; int topo; } Pilha;

void iniciaFila(Fila *f)  { f->ini = 0; f->fim = 0; f->qtd = 0; }
int  filaVazia(Fila *f)   { return f->qtd == 0; }
void Enfileira(Fila *f, int x) { f->v[f->fim] = x; f->fim = (f->fim + 1) % MAX; f->qtd++; }
int  Desenfileira(Fila *f) { int x = f->v[f->ini]; f->ini = (f->ini + 1) % MAX; f->qtd--; return x; }

void iniciaPilha(Pilha *p) { p->topo = 0; }
int  pilhaVazia(Pilha *p)  { return p->topo == 0; }
void Empilha(Pilha *p, int x) { p->v[p->topo++] = x; }
int  Desempilha(Pilha *p)  { return p->v[--p->topo]; }

/* Questão 3: inverte a fila F usando a pilha P (vazia) e uma variável aux */
void inverteFila(Fila *F, Pilha *P) {
    int aux;
    while (!filaVazia(F)) {      // fila -> pilha
        aux = Desenfileira(F);
        Empilha(P, aux);
    }
    while (!pilhaVazia(P)) {     // pilha -> fila (ordem invertida)
        aux = Desempilha(P);
        Enfileira(F, aux);
    }
}

int main() {
    Fila F; Pilha P;
    iniciaFila(&F); iniciaPilha(&P);
    for (int i = 1; i <= 5; i++) Enfileira(&F, i);
    inverteFila(&F, &P);
    while (!filaVazia(&F)) printf("%d ", Desenfileira(&F));   // 5 4 3 2 1
    printf("\n");
    return 0;
}
