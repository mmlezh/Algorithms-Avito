def hash_poly(text: str, size: int, p: int = 31) -> int:
    hash = 0
    power = 1

    for c in text:
        hash= (hash + ord(c) * power) % size
        power = (power * p) % size

    return hash


class HashMap:
    def __init__(self) -> None:
        self.cap= 8
        self.buckets = [[] for _ in range(self.cap)]
        self.size = 0

    def _index(self, key: str) -> int:
        return hash_poly(key, self.cap)

    def _resize(self) -> None:
        old_buckets = self.buckets

        self.cap *= 2
        self.buckets = [[] for _ in range(self.cap)]

        for bucket in old_buckets:
            for key, value in bucket:
                self.buckets[self._index(key)].append((key, value))

    def put(self, key: str, value: int) -> None:
        bucket = self.buckets[self._index(key)]

        for ind, (tmp_key, _) in enumerate(bucket):
            if tmp_key == key:
                bucket[ind] = (key, value)
                return
            
        if (self.size + 1) / self.cap > 0.7:
            self._resize()
            bucket = self.buckets[self._index(key)]

        bucket.append((key, value))
        self.size += 1

    def get(self, key: str) -> int:
        bucket = self.buckets[self._index(key)]

        for tmp_key, value in bucket:
            if tmp_key == key:
                return value

        return None

    def remove(self, key: str) -> int:
        bucket = self.buckets[self._index(key)]

        for ind, (tmp_key, value) in enumerate(bucket):
            if tmp_key == key:
                bucket.pop(ind)
                self.size -= 1
                return value

        return None


def main() -> None:
    n = int(input())
    table = HashMap()
    result = []

    for _ in range(n):
        command = input().split()

        if command[0] == "put":
            table.put(command[1], int(command[2]))
        elif command[0] == "get":
            value = table.get(command[1])
            result.append("Error" if value is None else str(value))
        elif command[0] == "del":
            value = table.remove(command[1])
            result.append("Error" if value is None else str(value))
        else:
            result.append(str(table.size))

    if result:
        print("\n".join(result))


if __name__ == "__main__":
    main()
