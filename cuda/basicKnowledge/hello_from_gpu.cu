// how to use gpu, how to write kernel function.
// what is block and grid.
// what is warp and how to get warpSize.
#include <stdio.h>

__global__ void hello() {
    printf("hello world from gpu!\n");
    printf("warpSize: %d", warpSize);
}

int main() {
    dim3 block(1, 2);
    dim3 grid(1, 2);
    hello<<<grid, 1>>>();
    cudaDeviceSynchronize();
    return 0;
}