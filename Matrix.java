import java.io.FileWriter;
import java.io.IOException;
import java.util.Random;

public class Matrix {
    public static void main(String[] args) {
        int[] sizes = {64, 128, 256, 512, 768, 1024, 1536, 2048};
        int RUNS = 5;
        Random rand = new Random();

        try {
            java.io.File resultsDir = new java.io.File("results");
            if (!resultsDir.exists()) resultsDir.mkdirs();

            try (FileWriter writer = new FileWriter("results/java_results.txt")) {
                for (int n : sizes) {
                    double[] times = new double[RUNS];
                    writer.write(String.format("%n=== Matrix size: %d x %d ===%n", n, n));
                    System.out.printf("%n=== Matrix size: %d x %d ===%n", n, n);

                    for (int r = 0; r < RUNS; r++) {
                        double[][] A = new double[n][n];
                        double[][] B = new double[n][n];
                        double[][] C = new double[n][n];

                        for (int i = 0; i < n; i++) {
                            for (int j = 0; j < n; j++) {
                                A[i][j] = rand.nextDouble();
                                B[i][j] = rand.nextDouble();
                            }
                        }

                        long start = System.nanoTime();
                        for (int i = 0; i < n; i++) {
                            for (int j = 0; j < n; j++) {
                                for (int k = 0; k < n; k++) {
                                    C[i][j] += A[i][k] * B[k][j];
                                }
                            }
                        }
                        long end = System.nanoTime();

                        double seconds = (end - start) / 1e9;
                        times[r] = seconds;
                        writer.write(String.format("Run %d: %.3f s%n", r + 1, seconds));
                        System.out.printf("Run %d: %.3f s%n", r + 1, seconds);
                    }

                    double sum = 0;
                    for (double t : times) sum += t;
                    double mean = sum / RUNS;
                    writer.write(String.format("Mean (%dx%d): %.3f s%n", n, n, mean));
                    System.out.printf("Mean (%dx%d): %.3f s%n", n, n, mean);
                }
            }
        } catch (IOException e) {
            System.out.println("Error writing results: " + e.getMessage());
        }
    }
}
