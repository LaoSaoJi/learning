#include <cuda_runtime.h>
#include <stdio.h>

int main() {
    int size = 10 * sizeof(int);
    int* d_data;
    cudaError_t cudaError = cudaMalloc((void**)&d_data, size);
    if (cudaError != cudaSuccess) {
        printf("cudaMalloc failed: %s\n", cudaGetErrorString(cudaError));
        return 1;
    }
    printf("cudaMalloc succeeded, d_data\n");
    cudaFree(d_data);
}