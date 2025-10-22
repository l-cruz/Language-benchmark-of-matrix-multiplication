#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define RUNS 5

int main() {
    int sizes[] = {64, 128, 256, 512, 768, 1024, 1536, 2048};
    int num_sizes = sizeof(sizes) / sizeof(sizes[0]);

    FILE *file = fopen("results/c_results.txt", "w");
    if (!file) {
        printf("Error opening results file.\n");
        return 1;
    }

    for (int s = 0; s < num_sizes; s++) {
        int N = sizes[s];
        double times[RUNS];
        fprintf(file, "\n=== Matrix size: %d x %d ===\n", N, N);
        printf("\n=== Matrix size: %d x %d ===\n", N, N);

        for (int r = 0; r < RUNS; r++) {
            double (*a)[N] = malloc(sizeof(double[N][N]));
            double (*b)[N] = malloc(sizeof(double[N][N]));
            double (*c)[N] = malloc(sizeof(double[N][N]));

            if (!a || !b || !c) {
                printf("Memory allocation failed for size %d.\n", N);
                return 1;
            }

            srand((unsigned) time(NULL));
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    a[i][j] = (double) rand() / RAND_MAX;
                    b[i][j] = (double) rand() / RAND_MAX;
                    c[i][j] = 0.0;
                }
            }

            clock_t start = clock();

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    for (int k = 0; k < N; k++) {
                        c[i][j] += a[i][k] * b[k][j];
                    }
                }
            }

            clock_t end = clock();
            double seconds = (double)(end - start) / CLOCKS_PER_SEC;
            times[r] = seconds;

            fprintf(file, "Run %d: %.3f s\n", r + 1, seconds);
            printf("Run %d: %.3f s\n", r + 1, seconds);

            free(a);
            free(b);
            free(c);
        }

        double sum = 0.0;
        for (int i = 0; i < RUNS; i++) sum += times[i];
        double mean = sum / RUNS;

        fprintf(file, "Mean (%dx%d): %.3f s\n", N, N, mean);
        printf("Mean (%dx%d): %.3f s\n", N, N, mean);
    }

    fclose(file);
    return 0;
}