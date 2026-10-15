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

def create_tree(root: AvlNode | None, key: int) -> AvlNode:
    if root is None:
        return AvlNode(key)

    if key < root.key:
        root.left = create_tree(root.left, key)
    else:
        root.right = create_tree(root.right, key)

    update(root)
    return root

def rotate_at(root: AvlNode, key: int, direction: str) -> AvlNode:
    if key < root.key:
        assert root.left is not None
        root.left = rotate_at(root.left, key, direction)
        update(root)
        return root

    if key > root.key:
        assert root.right is not None
        root.right = rotate_at(root.right, key, direction)
        update(root)
        return root

    if direction == "left":
        return rotate_left(root)
    return rotate_right(root)

def print_tree(root: AvlNode | None) -> list[int]:
    if root is None:
        return []

    return [root.key] + print_tree(root.left) + print_tree(root.right)

def main() -> None:
    node_count = int(input())
    keys = list(map(int, input().split()))
    root = None
  
    for key in keys:
        root = create_tree(root, key)

    rotation_count = int(input())

    for _ in range(rotation_count):
        direction, key_text = input().split()
        key = int(key_text)

        assert root is not None
        root = rotate_at(root, key, direction)

        result = print_tree(root)
        print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
