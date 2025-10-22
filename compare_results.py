import re
import matplotlib.pyplot as plt
import os


files = {
    "Python": "results/python_results.txt",
    "C": "results/c_results.txt",
    "Java": "results/java_results.txt"
}

results = {}

pattern = re.compile(r"Mean\s*\((\d+)x\1\):\s*([\d.]+)")

for lang, path in files.items():
    if not os.path.exists(path):
        print(f"File not found: {path}")
        continue
    sizes, means = [], []
    with open(path) as f:
        for line in f:
            m = pattern.search(line)
            if m:
                sizes.append(int(m.group(1)))
                means.append(float(m.group(2)))
    results[lang] = (sizes, means)
    print(f"Loaded {lang}: {len(sizes)} points")

plt.figure(figsize=(8,5))
for lang, (sizes, means) in results.items():
    plt.plot(sizes, means, marker="o", label=lang)

plt.title("Matrix Multiplication Benchmark Comparison")
plt.xlabel("Matrix size (N x N)")
plt.ylabel("Average time (s)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.tight_layout()

os.makedirs("results", exist_ok=True)
plt.savefig("results/comparison_plot.png", dpi=200)
plt.show()