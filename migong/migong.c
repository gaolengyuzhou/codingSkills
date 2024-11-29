#include <stdio.h>
#include <stdlib.h>

// 函数声明
void inputMatrix(int **matrix, int m, int n);
void freeMatrixMemory(int **matrix, int m);

int main() {
    int m, n;

    // 获取矩阵的行数和列数
    printf("请输入矩阵的行数m: ");
    scanf("%d", &m);

    printf("请输入矩阵的列数n: ");
    scanf("%d", &n);

    // 动态分配二维矩阵内存
    int **matrix = (int **)malloc(m * sizeof(int *));
    for (int i = 0; i < m; i++) {
        matrix[i] = (int *)malloc(n * sizeof(int));
    }

    // 输入矩阵元素
    inputMatrix(matrix, m, n);



    // 释放动态分配的内存
    freeMatrixMemory(matrix, m);

    return 0;
}

// 输入矩阵元素的函数
void inputMatrix(int **matrix, int m, int n) {
    printf("请按行输入矩阵元素（每行元素用空格隔开）:\n");
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%d", &matrix[i][j]);
        }
    }
}

// 释放二维矩阵内存的函数
void freeMatrixMemory(int **matrix, int m) {
    for (int i = 0; i < m; i++) {
        free(matrix[i]);
    }
    free(matrix);
}
