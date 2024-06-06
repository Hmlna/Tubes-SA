import time
import random
import matplotlib.pyplot as plt

def DP(price, n):
    val = [0 for _ in range(n + 1)]
    cuts = [[] for _ in range(n + 1)]

    for i in range(1, n + 1):
        max_val = float('-inf')
        best_cut = []
        for j in range(i):
            if price[j] + val[i-j-1] > max_val:
                max_val = price[j] + val[i-j-1]
                best_cut = cuts[i-j-1] + [j+1]
        val[i] = max_val
        cuts[i] = best_cut

    return val[n], cuts[n]

def Brute_Force(price, n):
    if n == 0:
        return 0, []
    max_val = float('-inf')
    best_cut = None

    for i in range(1, n + 1):
        val, cuts = Brute_Force(price, n - i)
        if price[i - 1] + val > max_val:
            max_val = price[i - 1] + val
            best_cut = cuts + [i]

    return max_val, best_cut

if __name__ == "__main__":
    n = input('Masukan kg daging: ')
    n = int(n)
    
    if n >= 16 and n <23:
        x = random.sample(range(2, 150), n)
    elif n >= 6 and n <16:
        x = random.sample(range(2, 100), n)
    elif n >= 1 and n <6:
        x = random.sample(range(2, 50), n)
    else:
        print('Maaf, daging terlalu berat')
        exit()
    x.sort()
    print("Harga potongan:", x)

    BeratDagings = range(1, n + 1)
    dp_times = []
    bf_times = []
    
    max_valueDP, selected_cutsDP, max_valueBF, selected_cutsBF = None, None, None, None

    for BeratDaging in BeratDagings:
        startDP = time.perf_counter()
        max_valueDP, selected_cutsDP = DP(x, BeratDaging)
        endDP = time.perf_counter()
        dp_times.append(endDP - startDP)

        startBF = time.perf_counter()
        max_valueBF, selected_cutsBF = Brute_Force(x, BeratDaging)
        endBF = time.perf_counter()
        bf_times.append(endBF - startBF)

    
    print(f"Berat daging: {BeratDaging}")
    print(f"DP - Max value: {max_valueDP}, Selected cuts: {selected_cutsDP}, Time: {endDP - startDP:.6f} seconds")
    print(f"BF - Max value: {max_valueBF}, Selected cuts: {selected_cutsBF}, Time: {endBF - startBF:.6f} seconds")
    print()

    plt.figure(figsize=(10, 5))
    plt.plot(BeratDagings, dp_times, label="Dynamic Programming", marker='o')
    plt.plot(BeratDagings, bf_times, label="Brute Force", marker='o')
    plt.xlabel("Berat Daging")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Execution Time of Dynamic Programming vs Brute Force")
    plt.legend()
    plt.grid(True)
    plt.xticks(BeratDagings)
    plt.show()