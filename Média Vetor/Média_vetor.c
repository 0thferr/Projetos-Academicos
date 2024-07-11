#include <stdio.h>
int main() {
 float vetor[15];
 float media = 0;

 // preenche o vetor com os 15 números reais
 for (int i = 0; i < 15; i++) {
 printf("Digite o %dº número: ", i+1);
 scanf("%f", &vetor[i]);
 media += vetor[i];
 }

 // calcula a média
 media /= 15;

 // exibe os números maiores que a média
 printf("\nNúmeros maiores que a média %.2f:\n", media);
 for (int i = 0; i < 15; i++) {
 if (vetor[i] > media) {
 printf("%.2f ", vetor[i]);
 }
 }

 return 0;
}