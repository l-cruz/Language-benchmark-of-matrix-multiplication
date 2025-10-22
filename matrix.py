import numpy as np
import time
import os

# Tamaños de matrices a probar
sizes = [64, 128, 256, 512, 768, 1024, 1536, 2048]
# Número de repeticiones por tamaño
runs = 5

os.makedirs("results", exist_ok=True)

# Archivo de salida
with open("results/python_results.txt", "w") as f:
    for n in sizes:
        times = []
        f.write(f"\n=== Matrix size: {n} x {n} ===\n")
        print(f"\n=== Matrix size: {n} x {n} ===")

        for r in range(runs):
            # Genera dos matrices aleatorias de tamaño n x n
            A = np.random.rand(n, n)
            B = np.random.rand(n, n)

            # Multiplicación y medición del tiempo
            start = time.time()
            C = np.dot(A, B)
            end = time.time()

            elapsed = round(end - start, 3)
            times.append(elapsed)

            print(f"Run {r+1}: {elapsed} s")
            f.write(f"Run {r+1}: {elapsed} s\n")

        # Promedio de las ejecuciones
        mean_time = round(sum(times) / runs, 3)
        print(f"Mean ({n}x{n}): {mean_time} s")
        f.write(f"Mean ({n}x{n}): {mean_time} s\n")
