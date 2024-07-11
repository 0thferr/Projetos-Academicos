#include <stdio.h> 
#include <stdlib.h> 
#include <time.h> 

int vence(int j, int v){ 
    while(v){ 
        if(j == (v % 10)){ 
            return 1; 
        } 
        v /= 10; 
    } 
    return 0; 
} 

int main() { 
    int matriz[5][2] = { 
        {0,342},{1,40},{2,31},{3,41},{4,20} 
    }; 
    int usuario, computador; 
    srand(time(0)); 
    while(1){ 
        printf("%s", 
            "0 = Pedra\n" 
            "1 = Papel\n" 
            "2 = Tesoura\n" 
            "3 = Lagarto\n" 
            "4 = Spock\n: " 
        ); 
        computador = rand() % 5; 
        scanf("%d",&usuario); 
        if(!(usuario >= 0 && usuario <= 4)){ 
            break; 
        } 
        printf("\nCOMPUTADOR = %d" 
            ", USUARIO = %d\n",computador,usuario); 
        if(vence(matriz[computador][0], 
            matriz[usuario][1])){ 
                printf("O USUARIO VENCEU\n"); 
        }else if(vence(matriz[usuario][0], 
            matriz[computador][1])){ 
                printf("O COMPUTADOR VENCEU\n"); 
        } 
    } 
    return 0; 

} 