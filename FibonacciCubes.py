t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    # Fibonacci
    fib = [1, 2]
    for _ in range(2, n + 1):
        fib.append(fib[-1] + fib[-2])

    result = []

    for _ in range(m):
        dims = sorted(map(int, input().split()))

        if dims[0] >= fib[n - 1] and dims[1] >= fib[n - 1] and dims[2] >= fib[n]:
            result.append("1")
        else:
            result.append("0")

    print("".join(result))