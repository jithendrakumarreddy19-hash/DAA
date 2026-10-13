"""
CSA06 - Design and Analysis of Algorithms
CO1 Assessment Tool 1: Scalability Audit of "ShopSphere"

This script checks the hand derivations in Solution.pdf by brute force:
  1. Runs the M1 and M2 loops and compares the counts with the formulas.
  2. Checks the closed forms for the S2, M4 and M5 recurrences.
  3. Checks the S1 average-case formula by simulation.
  4. Checks the constants chosen for the Theta(n^2) proof of f(n).
  5. Estimates operations and running time for n = 100,000 and 1,000,000
     and draws Output.png.

Run:     python Python_Code.py
Needs:   Python 3.8+ and matplotlib   (pip install matplotlib)
"""

import math
import random
from functools import lru_cache
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OPS_PER_SEC = 10**8        # ASSUMPTION: the exponent is blank in the question paper.
WINDOW_SEC = 10 * 60       # nightly window: 10 minutes
SIZES = [100_000, 1_000_000]


# ---------------------------------------------------------------- module code
def m1_count(n):
    """Run the M1 loops and count how often the IF condition is tested."""
    count = 0
    for i in range(0, n - 1):            # i = 0 .. n-2
        for j in range(i + 1, n):        # j = i+1 .. n-1
            count += 1
    return count


def m2_count(n):
    """Run the M2 loops and count the Audit operations."""
    count, i = 0, 1
    while i < n:
        for _ in range(i):               # j = 0 .. i-1
            count += 1
        i *= 2
    return count


@lru_cache(maxsize=None)
def t_s2(n):                             # T(n) = T(n/2) + 1, T(1) = 1
    return 1 if n == 1 else t_s2(n // 2) + 1


@lru_cache(maxsize=None)
def t_m4_now(n):                         # T(n) = 4T(n/2) + n, T(1) = 1
    return 1 if n == 1 else 4 * t_m4_now(n // 2) + n


@lru_cache(maxsize=None)
def t_m4_new(n):                         # T(n) = 2T(n/2) + n, T(1) = 1
    return 1 if n == 1 else 2 * t_m4_new(n // 2) + n


@lru_cache(maxsize=None)
def t_m5(n):                             # T(n) = 2T(n/2) + n log2 n, T(1) = 1
    return 1 if n == 1 else 2 * t_m5(n // 2) + n * (n.bit_length() - 1)


def f_report(n):
    return 3 * n * n + 10 * n * math.log2(n) + 50


# ------------------------------------------------------- closed-form formulas
def ops_m1(n):  return n * (n - 1) / 2
def ops_m2(n):  return 2 ** math.ceil(math.log2(n)) - 1
def ops_s2(n):  return math.floor(math.log2(n)) + 1
def ops_m4_now(n): return 2 * n * n - n
def ops_m4_new(n): return n * math.log2(n) + n
def ops_m5(n):
    L = math.log2(n)
    return n * L * (L + 1) / 2 + n


# ------------------------------------------------------------------ the checks
def run_checks():
    for n in [2, 5, 10, 50, 200]:
        assert m1_count(n) == n * (n - 1) // 2
    print("M1: loop count = n(n-1)/2 for n = 2, 5, 10, 50, 200 ... OK")

    for n in [2, 3, 5, 100, 1000, 1024, 1025, 5000]:
        assert m2_count(n) == 2 ** math.ceil(math.log2(n)) - 1
        assert n - 1 <= m2_count(n) <= 2 * n - 3
    print(f"M2: loop count = 2^ceil(log2 n) - 1, and n-1 <= count <= 2n-3 ... OK")
    print(f"M2 at n = 1,024: Audit count = {m2_count(1024)}  "
          f"(n - 1 = 1,023;  n log2 n would be {1024 * 10:,})")

    for n in range(1, 5000):
        assert t_s2(n) == n.bit_length()           # floor(log2 n) + 1
    print("S2: T(n) = floor(log2 n) + 1 for every n from 1 to 4,999 ... OK")

    for k in range(0, 13):
        n = 2 ** k
        assert t_m4_now(n) == 2 * n * n - n
        assert t_m4_new(n) == n * k + n
        assert t_m5(n) == n * k * (k + 1) // 2 + n
    print("M4: T(n) = 2n^2 - n and T(n) = n log2 n + n ... OK (n = 1 .. 4,096)")
    print("M5: T(n) = n log2 n (log2 n + 1) / 2 + n ... OK (n = 1 .. 4,096)")

    for n in range(8, 20_000):
        assert 3 * n * n <= f_report(n) <= 14 * n * n
    print("f(n): 3n^2 <= f(n) <= 14n^2 for every n from 8 to 19,999 ... OK")
    print(f"f(n)/n at n = 10^3, 10^5, 10^7: "
          + ", ".join(f"{f_report(10**e) / 10**e:,.0f}" for e in (3, 5, 7)) + "  (keeps growing, so not O(n))")

    random.seed(1)
    n, p, trials = 1000, 0.5, 200_000
    total = 0
    for _ in range(trials):
        total += random.randint(1, n) if random.random() < p else n
    formula = n * (1 - p / 2) + p / 2
    print(f"S1 average (n = 1,000, p = 0.5): simulated {total / trials:.1f}, formula {formula:.2f}")
    assert abs(total / trials - formula) / formula < 0.01


def estimate_table():
    modules = [
        ("M1 duplicate detector", ops_m1),
        ("M2 API rate limiter", ops_m2),
        ("S2 binary search (1 search)", ops_s2),
        ("M4 current  4T(n/2)+n", ops_m4_now),
        ("M4 redesign 2T(n/2)+n", ops_m4_new),
        ("M5 analytics 2T(n/2)+n log n", ops_m5),
        ("M5 report generator f(n)", f_report),
    ]
    print(f"\nAssumed speed: {OPS_PER_SEC:.0e} operations per second; window = {WINDOW_SEC} s")
    print(f"{'Module':<30}{'ops, n=100,000':>18}{'ops, n=1,000,000':>20}"
          f"{'time (s)':>14}{'time @10x speed':>17}  Fits 10 min?")
    rows = []
    for name, fn in modules:
        o1, o2 = fn(SIZES[0]), fn(SIZES[1])
        t, t10 = o2 / OPS_PER_SEC, o2 / (OPS_PER_SEC * 10)
        fits = "yes" if t <= WINDOW_SEC else "NO"
        print(f"{name:<30}{o1:>18,.4g}{o2:>20,.4g}{t:>14,.3g}{t10:>17,.3g}  {fits}")
        rows.append((name, fn, o2, t))
    return rows


def draw_graph(rows):
    ns = [int(10 ** (k / 4)) for k in range(8, 25)]       # 100 .. 1,000,000
    fig, ax = plt.subplots(1, 2, figsize=(14, 5.5))
    budget = OPS_PER_SEC * WINDOW_SEC
    for name, fn, _, _ in rows:
        if name.startswith("S2"):
            continue
        ax[0].plot(ns, [fn(n) for n in ns], label=name)
    ax[0].axhline(budget, color="black", linestyle="--")
    ax[0].text(3e5, budget * 1.6, "10-minute budget", fontsize=9)
    ax[0].set(xscale="log", yscale="log", xlabel="n (products)", ylabel="basic operations",
              title="Growth of each module")
    ax[0].grid(True, which="both", alpha=0.3)
    ax[0].legend(fontsize=8, loc="lower right")

    names = ["M1", "M2", "S2", "M4\ncurrent", "M4\nredesign", "M5\nanalytics", "M5\nreport"]
    times = [max(r[3], 1e-8) for r in rows]
    colors = ["tab:red" if t > WINDOW_SEC else "tab:green" for t in times]
    ax[1].bar(range(len(rows)), times, color=colors)
    ax[1].axhline(WINDOW_SEC, color="black", linestyle="--")
    ax[1].text(1.6, WINDOW_SEC * 1.6, "10-minute window", fontsize=9)
    ax[1].set_yscale("log")
    ax[1].set_xticks(range(len(rows)))
    ax[1].set_xticklabels(names, fontsize=9)
    ax[1].set(ylabel="seconds (log scale)", title="Running time at n = 1,000,000")
    fig.suptitle(f"ShopSphere scalability audit ({OPS_PER_SEC:.0e} operations per second assumed)", fontsize=13)
    fig.tight_layout()
    fig.savefig("Output.png", dpi=150)
    print("\nGraph saved to Output.png")


if __name__ == "__main__":
    run_checks()
    draw_graph(estimate_table())