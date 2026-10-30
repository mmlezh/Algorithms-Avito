def solve() -> None:
    n, k = map(int, input().split())
    ids = list(map(int, input().split()))
    freqs = {}

    for id in ids[:k]:
        freqs[id] = freqs.get(id, 0) + 1

    result = [len(freqs)]

    for i in range(k, n):
        freqs[ids[i - k]] -= 1
        if freqs[ids[i - k]] == 0:
            del freqs[ids[i - k]]

        freqs[ids[i]] = freqs.get(ids[i], 0) + 1
        result.append(len(freqs))

    print(*result)


if __name__ == "__main__":
    solve()
