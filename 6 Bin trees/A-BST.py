from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Node:
    key: int
    left: Node | None = None
    right: Node | None = None

def insert(root: Node | None, key: int, verbose: bool = True) -> Node:
    if root is None:
        return Node(key)
    current = root
    while True:
        if key == current.key:
            return root
        if key < current.key:
            if current.left is None:
                current.left = Node(key)
                return root
            current = current.left
        else:
            if current.right is None:
                current.right = Node(key)
                return root
            current = current.right

def search(root: Node | None, key: int) -> Node | None:
    current = root
    while current is not None:
        if key == current.key:
            return current
        if key < current.key:
            current = current.left
        else:
            current = current.right
    return None

def find_min(root: Node | None) -> Node | None:
    if root is None:
        return None
    current = root
    while current.left is not None:
        current = current.left
    return current

def delete_node(root: Node | None, key: int) -> Node | None:
    if root is None:
        return None
    if key < root.key:
        root.left = delete_node(root.left, key)
        return root
    if key > root.key:
        root.right = delete_node(root.right, key)
        return root

    if root.left is None and root.right is None:
        return None
    if root.left is None:
        return root.right
    if root.right is None:
        return root.left

    succ = find_min(root.right)
    assert succ is not None
    root.key = succ.key
    root.right = delete_node(root.right, succ.key)
    return root

def tree_height(root: Node | None) -> int:
    if root is None:
        return 0
    return 1 + max(tree_height(root.left), tree_height(root.right))

def print_tree(root: Node | None) -> list[int]:
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
            root = insert(root, int(parts[1]), verbose=False)
        elif command == "del":
            root = delete_node(root, int(parts[1]))
        elif command == "exists":
            node = search(root, int(parts[1]))
            print("YES" if node is not None else "NO")
        elif command == "height":
            print(tree_height(root))
        else:
            result = print_tree(root)
            print(" ".join(map(str, result)) if result else "Empty")

if __name__ == "__main__":
    main()
