from __future__ import annotations

from dataclasses import dataclass

@dataclass
class AvlNode:
    key: int
    left: AvlNode | None = None
    right: AvlNode | None = None
    height: int = 0

def height(node: AvlNode | None) -> int:
    return -1 if node is None else node.height

def update(node: AvlNode) -> None:
    node.height = 1 + max(height(node.left), height(node.right))

def balance_factor(node: AvlNode) -> int:
    return height(node.left) - height(node.right)

def rotate_right(y: AvlNode) -> AvlNode:
    x = y.left
    assert x is not None
    y.left = x.right
    x.right = y
    update(y)
    update(x)
    return x

def rotate_left(x: AvlNode) -> AvlNode:
    y = x.right
    assert y is not None
    x.right = y.left
    y.left = x
    update(x)
    update(y)
    return y

def avl_insert(root: AvlNode | None, key: int) -> AvlNode:
    if root is None:
        return AvlNode(key)

    if key == root.key:
        return root

    if key < root.key:
        root.left = avl_insert(root.left, key)
    else:
        root.right = avl_insert(root.right, key)

    update(root)
    bf = balance_factor(root)

    if bf > 1 and key < root.left.key:
        return rotate_right(root)

    if bf < -1 and key > root.right.key:
        return rotate_left(root)

    if bf > 1 and key > root.left.key:
        root.left = rotate_left(root.left)
        return rotate_right(root)

    if bf < -1 and key < root.right.key:
        root.right = rotate_right(root.right)
        return rotate_left(root)

    return root

def find_min(root: AvlNode) -> AvlNode:
    current = root
    while current.left is not None:
        current = current.left
    return current

def avl_delete(root: AvlNode | None, key: int) -> AvlNode | None:
    if root is None:
        return None

    if key < root.key:
        root.left = avl_delete(root.left, key)
    elif key > root.key:
        root.right = avl_delete(root.right, key)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left

        successor = find_min(root.right)
        root.key = successor.key
        root.right = avl_delete(root.right, successor.key)

    update(root)
    bf = balance_factor(root)

    if bf > 1 and balance_factor(root.left) >= 0:
        return rotate_right(root)

    if bf < -1 and balance_factor(root.right) <= 0:
        return rotate_left(root)

    if bf > 1 and balance_factor(root.left) < 0:
        root.left = rotate_left(root.left)
        return rotate_right(root)

    if bf < -1 and balance_factor(root.right) > 0:
        root.right = rotate_right(root.right)
        return rotate_left(root)

    return root

def search(root: AvlNode | None, key: int) -> AvlNode | None:
    current = root
    while current is not None:
        if key == current.key:
            return current
        if key < current.key:
            current = current.left
        else:
            current = current.right
    return None

def find_next(root: AvlNode | None, key: int) -> AvlNode | None:
    current = root
    answer = None

    while current is not None:
        if current.key >= key:
            answer = current
            current = current.left
        else:
            current = current.right

    return answer

def find_prev(root: AvlNode | None, key: int) -> AvlNode | None:
    current = root
    answer = None

    while current is not None:
        if current.key <= key:
            answer = current
            current = current.right
        else:
            current = current.left

    return answer

def print_tree(root: AvlNode | None) -> list[int]:
    if root is None:
        return []

    return [root.key] + print_tree(root.left) + print_tree(root.right)

def main() -> None:
    command_count = int(input())
    root = None

    for _ in range(command_count):
        parts = input().split()
        command = parts[0]

        if command == "add":
            root = avl_insert(root, int(parts[1]))
        elif command == "del":
            root = avl_delete(root, int(parts[1]))
        elif command == "exists":
            node = search(root, int(parts[1]))
            print("YES" if node is not None else "NO")
        elif command == "next":
            node = find_next(root, int(parts[1]))
            print(node.key if node is not None else "None")
        elif command == "prev":
            node = find_prev(root, int(parts[1]))
            print(node.key if node is not None else "None")
        elif command == "root":
            print(root.key if root is not None else "Empty")
        elif command == "height":
            print(height(root) + 1)
        else:
            result = print_tree(root)
            print(" ".join(map(str, result)) if result else "Empty")

if __name__ == "__main__":
    main()
