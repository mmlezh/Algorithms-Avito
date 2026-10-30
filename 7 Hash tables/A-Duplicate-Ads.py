def solve() -> None:
    number_of_ads = int(input())

    group_sizes = {}

    for _ in range(number_of_ads):
        title = input().strip()
        key = "".join(sorted(title))
        group_sizes[key] = group_sizes.get(key, 0) + 1

    print(len(group_sizes), max(group_sizes.values()))


if __name__ == "__main__":
    solve()