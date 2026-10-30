def main() -> None:
    n, s = map(int, input().split())
    changes = list(map(int, input().split()))

    freqs = {0: 1}
    prefix_sum = 0
    result = 0

    for change in changes:
        prefix_sum += change
        result += freqs.get(prefix_sum - s, 0)
        freqs[prefix_sum] = freqs.get(prefix_sum, 0) + 1

    print(result)


if __name__ == "__main__":
    main()
